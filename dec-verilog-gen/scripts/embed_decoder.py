import sys
import os

def embed_instantiation(template_file, pla_files, output_file="mrt64_decoder.sv"):
    modules = {}
    all_signals = []
    
    # 1. 解析所有 PLA 文件，提取每个模块所属的输出信号
    for pla in pla_files:
        if not os.path.exists(pla):
            print(f"⚠️ 警告: 找不到 PLA 文件 '{pla}'，跳过。")
            continue
            
        mod_name = os.path.splitext(os.path.basename(pla))[0]
        outputs = []
        with open(pla, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('.ob'):
                    outputs = line.split()[1:]
                    break  # 找到输出定义后就可以跳出当前文件了
                    
        if outputs:
            modules[mod_name] = outputs
            for out in outputs:
                if out not in all_signals:
                    all_signals.append(out)

    if not all_signals:
        print("❌ 错误: 没有从 PLA 文件中提取到任何控制信号。")
        return

    # 2. 生成要替换进模板的 Verilog 代码块
    replace_lines = []
    
    # 按照模块生成 wire 定义和注释
    for mod, sigs in modules.items():
        replace_lines.append(f"// control signals from {mod}")
        replace_lines.append(f"wire {', '.join(sigs)};")
        
    replace_lines.append("// 例化 unified_wrapper 及连接代码")
    replace_lines.append("decoder_wrapper u_decoder_wrapper (")
    replace_lines.append("    .op(op),")
    
    # 生成端口映射
    for i, sig in enumerate(all_signals):
        comma = "," if i < len(all_signals) - 1 else ""
        replace_lines.append(f"    .{sig:<15} ({sig}){comma}")
    replace_lines.append(");")

    # 3. 读取模板并替换标志位
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_lines = f.readlines()
            
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in template_lines:
                if "`SCRIPT_INST_FLAG" in line:
                    # 提取原有缩进，保证生成的代码格式整齐对齐
                    indent = line[:line.find("`SCRIPT_INST_FLAG")]
                    for r_line in replace_lines:
                        # 如果是 block 内部的缩进，给例化内部加 4 个空格
                        if r_line.startswith("unified") or r_line.startswith("//"):
                            f.write(indent + r_line + "\n")
                        elif r_line.startswith("    ."):
                            f.write(indent + r_line + "\n")
                        else:
                            f.write(indent + r_line + "\n")
                else:
                    f.write(line)

        print(f"✅ 成功将例化代码嵌入到 '{output_file}' 中！")
        print(f"📦 接入的子模块: {', '.join(modules.keys())}")
        
    except FileNotFoundError:
        print(f"❌ 错误: 找不到模板文件 '{template_file}'")
    except Exception as e:
        print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 embed_decoder.py <模板.sv> <PLA文件1> <PLA文件2> ...")
    else:
        template = sys.argv[1]
        plas = sys.argv[2:]
        embed_instantiation(template, plas)
