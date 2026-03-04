import sys
import csv
import re

def pla_to_sysinst_csv(pla_file, csv_file):
    try:
        with open(pla_file, 'r', encoding='utf-8') as f_in, \
             open(csv_file, 'w', newline='', encoding='utf-8') as f_out:
            
            writer = csv.writer(f_out)
            # 写入你要求的标准 CSV 表头
            writer.writerow(['set name', 'inst name', 'mask', 'sysinstr_w'])
            
            current_set = "Default"
            current_inst = "Unknown"
            
            for line in f_in:
                line = line.strip()
                
                # 跳过空行和配置头（.i, .o, .ilb, .ob, .e 等）
                if not line or line.startswith('.'):
                    continue
                
                # 1. 提取 Set Name (匹配连续的 # 号包裹的标题)
                if line.startswith('###'):
                    clean_set = re.sub(r'#+', '', line).strip()
                    if clean_set:
                        current_set = clean_set
                    continue
                
                # 2. 提取 Inst Name
                # 如果以 # 开头，我们需要区分它是“指令名注释”还是“被注释掉的掩码”
                if line.startswith('#'):
                    content = line.lstrip('#').strip()
                    first_token = content.split()[0] if content else ""
                    
                    # 如果内容不是 32 位的掩码串，则认定为指令名
                    if not re.match(r'^[01\-]{32}$', first_token):
                        current_inst = first_token
                    continue
                    
                # 3. 提取 Mask 并写入数据
                # 有效的掩码行必定以 0, 1 或 - 开头
                if line[0] in ('0', '1', '-'):
                    parts = line.split()
                    mask = parts[0]
                    
                    # 确保提取到的是 32 位的完整掩码
                    if len(mask) == 32:
                        writer.writerow([current_set, current_inst, mask, 1])

        print(f"✅ 特权指令转换成功！")
        print(f"📄 输入: {pla_file}")
        print(f"🚀 输出: {csv_file}")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{pla_file}'")
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 pla2syscsv.py <输入.pla> <输出.csv>")
    else:
        pla_to_sysinst_csv(sys.argv[1], sys.argv[2])
