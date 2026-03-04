import sys
import os

def generate_wrapper(pla_file, wrapper_file=None):
    base_name = os.path.splitext(os.path.basename(pla_file))[0]
    
    if wrapper_file is None:
        wrapper_file = f"{base_name}_wrapper.v"
        
    # 默认 ABC 生成的核心模块名（带转义前缀和后缀空格）
    core_module_name = f"\\{base_name} "
    wrapper_module_name = f"{base_name}_wrapper"

    inputs = []
    outputs = []

    try:
        # 1. 解析 PLA 文件提取端口信息
        with open(pla_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('.ilb'):
                    inputs = line.split()[1:]
                elif line.startswith('.ob'):
                    outputs = line.split()[1:]

        if not inputs or not outputs:
            print("error:can not find defination of .lib or .ob in PLA file.")
            return

        # 2. 提取输入向量的基础名称和位宽范围
        # 假设输入格式为 op[31] ... op[0]
        first_in = inputs[0]
        last_in = inputs[-1]
        
        vec_name = first_in.split('[')[0]
        msb = int(first_in.split('[')[1].replace(']', ''))
        lsb = int(last_in.split('[')[1].replace(']', ''))

        # 3. 开始生成 Verilog Wrapper 代码
        v_lines = []
        v_lines.append(f"// Auto-generated Wrapper for ABC synthesized netlist")
        v_lines.append(f"// Source PLA: {pla_file}\n")
        
        v_lines.append(f"module {wrapper_module_name} (")
        v_lines.append(f"    input  [{msb}:{lsb}] {vec_name},")
        
        for i, out in enumerate(outputs):
            comma = "," if i < len(outputs) - 1 else ""
            v_lines.append(f"    output {out}{comma}")
        v_lines.append(");\n")

        # 4. 实例化底层核心模块
        v_lines.append(f"    // inst the opt file generate by ABC")
        v_lines.append(f"    {core_module_name} u_core_netlist (")
        
        # 输入端口映射（处理转义字符，注意转义字符后必须有空格）
        for inp in inputs:
            v_lines.append(f"        .\\{inp}  ({inp}),")
            
        # 输出端口映射
        for i, out in enumerate(outputs):
            comma = "," if i < len(outputs) - 1 else ""
            # 对齐格式使得代码美观
            v_lines.append(f"        .{out:<15} ({out}){comma}")
            
        v_lines.append("    );\n")
        v_lines.append("endmodule")

        # 5. 写入文件
        with open(wrapper_file, 'w') as f:
            f.write("\n".join(v_lines) + "\n")

        print(f"gen wrapper successful！")
        print(f"top module name: {wrapper_module_name}")
        print(f"outputfile: {wrapper_file}")

    except Exception as e:
        print(f"error:gen wrapper failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 gen_wrapper.py <inputfile.pla> [outputfile_wrapper.v]")
    else:
        pla_in = sys.argv[1]
        v_out = sys.argv[2] if len(sys.argv) > 2 else None
        generate_wrapper(pla_in, v_out)
