import sys
import csv
import re

def pla_to_csr_csv(pla_file, csv_file):
    try:
        with open(pla_file, 'r', encoding='utf-8') as f_in, \
             open(csv_file, 'w', newline='', encoding='utf-8') as f_out:
            
            writer = csv.writer(f_out)
            # 写入你要求的标准 CSV 表头
            writer.writerow(['set name', 'csr name', 'addr', 'legal_csr_w'])
            
            current_set = "Default"
            current_csr = "Unknown"
            
            for line in f_in:
                line = line.strip()
                
                # 跳过空行和配置头
                if not line or line.startswith('.i') or line.startswith('.o'):
                    continue
                
                # 1. 提取 Set Name (匹配连续的 # 号包裹的标题)
                if line.startswith('###'):
                    # 剥离所有的 # 号和两端空格
                    clean_set = re.sub(r'#+', '', line).strip()
                    if clean_set:
                        current_set = clean_set
                    continue
                
                # 2. 提取 CSR Name (匹配单个 # 开头的注释)
                if line.startswith('#') and not line.startswith('#.'):
                    # 取 # 号后的第一个单词作为 CSR 名字
                    parts = line.lstrip('#').split()
                    if parts:
                        current_csr = parts[0]
                    continue
                    
                # 3. 提取地址并写入数据 (匹配 0 或 1 开头的二进制行)
                if line[0] in ('0', '1'):
                    parts = line.split()
                    bin_addr = parts[0]
                    
                    if len(bin_addr) == 12:
                        # 将 12 位二进制直接转换为 3 位的 16 进制字符串，确保绝对准确
                        hex_addr = f"0x{int(bin_addr, 2):03x}"
                        
                        # legal_csr_w 强制置为 1
                        writer.writerow([current_set, current_csr, hex_addr, 1])

        print(f"✅ CSR 转换成功！")
        print(f"📄 输入: {pla_file}")
        print(f"🚀 输出: {csv_file}")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{pla_file}'")
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 pla2csv.py <输入.pla> <输出.csv>")
    else:
        pla_to_csr_csv(sys.argv[1], sys.argv[2])
