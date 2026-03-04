import sys
import csv
import os

def csv_to_csr_pla(input_csv, output_pla=None):
    if output_pla is None:
        base_name = os.path.splitext(input_csv)[0]
        output_pla = f"{base_name}.pla"

    try:
        with open(input_csv, 'r', encoding='utf-8') as f_in:
            reader = csv.reader(f_in)
            # 跳过表头
            header = next(reader)

            pla_lines = []
            
            # --- 写入 PLA 头部 ---
            pla_lines.append("# mrt privilege decoder")
            pla_lines.append(".i 12")
            pla_lines.append(".o 1")
            # CSR 地址译码对应指令的 [31:20]
            pla_lines.append(".ilb op[31] op[30] op[29] op[28] op[27] op[26] op[25] op[24] op[23] op[22] op[21] op[20]")
            pla_lines.append(".ob legal_csr_w")
            pla_lines.append("#.type fr\n")

            # --- 解析每一行并写入数据 ---
            for row in reader:
                # 防错：跳过空行或格式不对的行
                if not row or len(row) < 4:
                    continue
                
                set_name = row[0].strip()
                csr_name = row[1].strip()
                hex_addr_str = row[2].strip()
                legal_csr_w = row[3].strip()

                # 将 16 进制字符串 (如 '0x300') 转换为整型，再格式化为 12 位二进制字符串
                try:
                    addr_int = int(hex_addr_str, 16)
                    bin_addr = f"{addr_int:012b}"
                except ValueError:
                    print(f"⚠️ 警告: 无法解析地址 '{hex_addr_str}'，跳过 {csr_name}")
                    continue

                # 格式化输出，保持 PLA 文件的整洁易读
                pla_lines.append(f"#{csr_name:<13} {hex_addr_str}")
                pla_lines.append(f"{bin_addr}  {legal_csr_w}")

            # --- 写入 PLA 尾部 ---
            pla_lines.append("")
            pla_lines.append(".e")

        # 写入文件
        with open(output_pla, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(pla_lines) + "\n")

        print(f"✅ CSR PLA 生成成功！")
        print(f"📄 输入: {input_csv}")
        print(f"🚀 输出: {output_pla}")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{input_csv}'")
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 csv2csrpla.py <输入文件.csv> [输出文件.pla]")
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else None
        csv_to_csr_pla(in_file, out_file)
