import csv
import sys
import os

def csv_to_pla(input_csv, output_pla=None):
    # 如果没有指定输出文件名，默认生成同名的 .pla 文件
    if output_pla is None:
        base_name = os.path.splitext(input_csv)[0]
        output_pla = f"{base_name}.pla"

    try:
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # 读取表头
            header = next(reader)

            # 输出信号列从第 4 列开始 (索引 3)
            out_labels = header[3:]
            num_outputs = len(out_labels)

            pla_lines = []
            pla_lines.append(f"# Generated PLA file from {input_csv}")
            
            # .i 和 .o 定义输入输出数量
            pla_lines.append(".i 32")
            pla_lines.append(f".o {num_outputs}")

            # .ilb 定义输入引脚名称 (op[31] 到 op[0])
            ilb_str = " ".join([f"op[{i}]" for i in range(31, -1, -1)])
            pla_lines.append(f".ilb {ilb_str}")

            # .ob 定义输出信号名称
            ob_str = " ".join(out_labels)
            pla_lines.append(f".ob {ob_str}")
            pla_lines.append("")

            # 遍历数据行
            for row in reader:
                # 跳过空行
                if not row:
                    continue
                
                inst_name = row[1].strip()
                mask = row[2].strip()
                
                # 提取控制信号，如果为空字符串则替换为 '0'
                signals = row[3:]
                
                # 防错机制：防止某些行末尾缺逗号导致列数不够
                while len(signals) < num_outputs:
                    signals.append('0')
                    
                clean_signals = ['0' if s.strip() == '' else s.strip() for s in signals]
                joined_signals = "".join(clean_signals)

                # 写入注释和数据行
                pla_lines.append(f"#{inst_name}")
                pla_lines.append(f"{mask} {joined_signals}")

            # 结束标志
            pla_lines.append("")
            pla_lines.append(".e")

        # 写入 PLA 文件
        with open(output_pla, 'w', encoding='utf-8') as f:
            f.write("\n".join(pla_lines) + "\n")

        print(f"trans successfully!")
        print(f"input: {input_csv}")
        print(f"output: {output_pla}")
        print(f"stats: 32 bits input, {num_outputs} control signals")

    except FileNotFoundError:
        print(f"error: can not find file '{input_csv}'")
    except Exception as e:
        print(f"error: trans failed {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python csv2pla.py <inputfile.csv> [outputfile.pla]")
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else None
        csv_to_pla(in_file, out_file)
