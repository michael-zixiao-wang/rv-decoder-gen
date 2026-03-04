import sys
import csv
import os

def csv_to_sys_pla(input_csv, output_pla=None):
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
            pla_lines.append(".i 32")
            pla_lines.append(".o 1")
            
            # 生成 op[31] 到 op[0] 的标签串
            ilb_str = " ".join([f"op[{i}]" for i in range(31, -1, -1)])
            pla_lines.append(f".ilb {ilb_str}")
            pla_lines.append(".ob sysinstr_w")
            pla_lines.append("#.type fr\n")

            # --- 解析每一行并写入数据 ---
            for row in reader:
                # 防错：确保该行数据完整
                if not row or len(row) < 4:
                    continue
                
                inst_name = row[1].strip()
                mask = row[2].strip()
                sysinstr_w = row[3].strip()

                # 写入带注释的数据行
                pla_lines.append(f"#{inst_name}")
                pla_lines.append(f"{mask} {sysinstr_w}")

            # --- 写入 PLA 尾部 ---
            pla_lines.append("")
            pla_lines.append(".e")

        # 写入文件
        with open(output_pla, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(pla_lines) + "\n")

        print(f"✅ Privilege PLA 生成成功！")
        print(f"📄 输入: {input_csv}")
        print(f"🚀 输出: {output_pla}")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{input_csv}'")
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 csv2syspla.py <输入文件.csv> [输出文件.pla]")
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else None
        csv_to_sys_pla(in_file, out_file)
