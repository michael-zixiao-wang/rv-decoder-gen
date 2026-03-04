import re
import csv
import sys
import os

def parse_base_instruction(line):
    line = line.strip()
    # 过滤注释和伪指令
    if not line or line.startswith('#') or line.startswith('$'):
        return None

    tokens = line.split()
    if not tokens:
        return None

    inst_name = tokens[0]
    # 提取位域和关键字
    body_tokens = tokens[1:]
    
    # --- 新增逻辑：识别寄存器有效信号 ---
    # 只要 tokens 中出现了对应的字样，就认为该信号有效
    rs1_valid = 1 if 'rs1' in body_tokens else 0
    rs2_valid = 1 if 'rs2' in body_tokens else 0
    rd_valid  = 1 if 'rd' in body_tokens else 0

    # 初始化 32 位掩码
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

    return inst_name, "".join(reversed(mask)), rs1_valid, rs2_valid, rd_valid

def main(input_file):
    # 修改 1：自动生成 .pla 后缀的默认文件名
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.csv"
    
    results = []
    try:
        with open(input_file, 'r') as f:
            for line in f:
                res = parse_base_instruction(line)
                if res:
                    results.append(res)

        # 写入文件
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # 修改 2：增加控制信号标题行
            writer.writerow(['inst name', 'mask', 'rs1_valid_w', 'rs2_valid_w', 'rd_valid_w'])
            writer.writerows(results)
            
        print(f"complete!")
        print(f"input file: {input_file}")
        print(f"output file: {output_file}")
        print(f"get instruction num: {len(results)}")

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 gen_mask.py <input_file>")
    else:
        main(sys.argv[1])
