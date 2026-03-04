import sys
import os

def generate_unified_wrapper(pla_files, wrapper_file="decoder_wrapper.sv"):
    modules = []
    all_outputs = []

    # 1. 遍历所有传入的 pla 文件，提取端口信息
    for pla_file in pla_files:
        try:
            base_name = os.path.splitext(os.path.basename(pla_file))[0]
            inputs = []
            outputs = []
            
            with open(pla_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('.ilb'):
                        inputs = line.split()[1:]
                    elif line.startswith('.ob'):
                        outputs = line.split()[1:]
            
            if not inputs or not outputs:
                print(f"⚠️ 警告: {pla_file} 缺少 .ilb 或 .ob，跳过该文件。")
                continue

            modules.append({
                'name': base_name,
                'inputs': inputs,
                'outputs': outputs
            })

            # 收集并去重所有输出信号
            for out in outputs:
                if out not in all_outputs:
                    all_outputs.append(out)
                    
        except FileNotFoundError:
            print(f"❌ 错误: 找不到文件 {pla_file}")
            continue

    if not modules:
        print("❌ 错误: 没有成功解析任何有效的 PLA 文件。")
        return

    wrapper_module_name = os.path.splitext(os.path.basename(wrapper_file))[0]

    # 2. 开始生成 Verilog 代码
    v_lines = []
    v_lines.append(f"// Auto-generated Unified Wrapper for ABC synthesized netlists")
    v_lines.append(f"// Included Modules: {', '.join([m['name'] for m in modules])}\n")
    
    v_lines.append(f"module {wrapper_module_name} (")
    # 强制统一使用 op[31:0]
    v_lines.append(f"    input  [31:0] op,")
    
    # 定义所有的输出信号
    for i, out in enumerate(all_outputs):
        comma = "," if i < len(all_outputs) - 1 else ""
        v_lines.append(f"    output {out}{comma}")
    v_lines.append(");\n")

    # 3. 实例化所有的底层模块
    for mod in modules:
        mod_name = mod['name']
        v_lines.append(f"    // ---------------------------------------------------------")
        v_lines.append(f"    // inst {mod_name} ")
        v_lines.append(f"    // ---------------------------------------------------------")
        v_lines.append(f"    \\{mod_name}  u_{mod_name} (")
        
        ports = []
        # 映射输入端口 (处理反斜杠转义和括号)
        for inp in mod['inputs']:
            ports.append(f"        .\\{inp}  ({inp})")
        
        # 映射输出端口
        for out in mod['outputs']:
            ports.append(f"        .{out:<15} ({out})")
            
        # 将端口连接用逗号和换行拼接
        v_lines.append(",\n".join(ports))
        v_lines.append("    );\n")
        
    v_lines.append("endmodule")

    # 4. 写入文件
    with open(wrapper_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(v_lines) + "\n")

    print(f"✅ Unified Wrapper 顶层生成成功！")
    print(f"📦 包含的子模块: {', '.join([m['name'] for m in modules])}")
    print(f"📄 输出文件: {wrapper_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 gen_unified_wrapper.py <文件1.pla> <文件2.pla> ... [可选择通过修改脚本更改默认输出名]")
    else:
        # 传入所有命令行参数作为 pla 文件列表
        generate_unified_wrapper(sys.argv[1:])
