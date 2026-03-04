## this file is designed to generate mask for float or double instructions
import re
import csv
import sys
import os

def parse_base_instruction(line):
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('$'):
        return None

    tokens = line.split()
    if not tokens:
        return None

    inst_name = tokens[0]
    body_tokens = tokens[1:]
    
    # 基础存在性检查
    has_rs1 = 'rs1' in body_tokens
    has_rs2 = 'rs2' in body_tokens
    has_rs3 = 'rs3' in body_tokens
    has_rd  = 'rd' in body_tokens

    # --- 浮点指令寄存器分类逻辑 ---
    
    # 1. 判断 rs1 是否属于 GPR (通用寄存器)
    # 包含：加载存储基址, fcvt.s.w(u), fcvt.d.w(u), fmv.w.x
    rs1_is_gpr = inst_name.startswith(('flw', 'fld', 'fsw', 'fsd', 'fcvt.s.', 'fcvt.d.', 'fmv.w.x'))
    
    # 2. 判断 rd 是否属于 GPR (通用寄存器)
    # 包含：fcvt.w(u).s, fcvt.l(u).d, fmv.x.w, feq, flt, fle, fclass
    rd_is_gpr = inst_name.startswith(('fcvt.w', 'fcvt.l', 'fmv.x', 'feq', 'flt', 'fle', 'fclass'))

    # 生成控制信号
    # GPR 信号
    rs1_valid = 1 if (has_rs1 and rs1_is_gpr) else 0
    rs2_valid = 0 # F/D 扩展中 rs2 通常不从 GPR 读取
    rd_valid  = 1 if (has_rd and rd_is_gpr) else 0
    
    # FPR 信号
    rs1_float_w = 1 if (has_rs1 and not rs1_is_gpr) else 0
    rs2_float_w = 1 if has_rs2 else 0 # F/D 中有 rs2 的基本都是 FPR
    rs3_float_w = 1 if has_rs3 else 0
    rd_float_w  = 1 if (has_rd and not rd_is_gpr) else 0

    # --- 32 位掩码解析 (保持不变) ---
    mask = ['-'] * 32
    range_pattern = re.compile(r'(\d+)\.\.(\d+)=(0x[0-9a-fA-F]+|\d+)')
    single_pattern = re.compile(r'(\d+)=(0x[0-9a-fA-F]+|\d+)')

    for token in body_tokens:
        range_match = range_pattern.match(token)
        single_match = single_pattern.match(token)

        if range_match:
            hi, lo = int(range_match.group(1)), int(range_match.group(2))
            val = int(range_match.group(3), 0)
            width = hi - lo + 1
            bin_val = format(val, f'0{width}b')
            for i, bit in enumerate(reversed(bin_val)):
                if lo + i < 32:
                    mask[lo + i] = bit
        elif single_match:
            bit_idx, val = int(single_match.group(1)), int(single_match.group(2), 0)
            if bit_idx < 32:
                mask[bit_idx] = str(val & 1)

    return (inst_name, "".join(reversed(mask)), 
            rs1_valid, rs2_valid, rd_valid, 
            rs1_float_w, rs2_float_w, rs3_float_w, rd_float_w)

def main(input_file):
    base_name = os.path.splitext(input_file)[0]
    # 修正了后缀为 .csv
    output_file = f"{base_name}.csv"
    
    results = []
    try:
        with open(input_file, 'r') as f:
            for line in f:
                res = parse_base_instruction(line)
                if res:
                    results.append(res)

        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # 按照你要求的顺序拼在后面
            writer.writerow(['inst name', 'mask', 
                             'rs1_valid', 'rs2_valid', 'rd_valid', 
                             'rs1_float_w', 'rs2_float_w', 'rs3_float_w', 'rd_float_w'])
            writer.writerows(results)
            
        print(f"Complete!")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        print(f"Processed {len(results)} instructions.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 gen_fp_mask.py <input_file>")
    else:
        main(sys.argv[1])
