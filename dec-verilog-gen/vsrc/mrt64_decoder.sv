`include "mrt64_defs.svh"

module mrt64_decoder
import mrt64_pkg::*;
(
 input                        valid_i
 ,input                        fetch_fault_i
 ,input  [31:0]                opcode_i
 ,input  [1:0]                 priv_i

 ,output dec_t                 dec_o
 ,output                       instr_br_o
 ,output                       instr_call_o
 ,output                       instr_ret_o
 ,output                       instr_jmp_o
 );


/// rename
wire [31:0] op;
assign op = opcode_i;


/// basic decode
// control signals from dec_opt
wire exec_w, lsu_w, branch_w, mul_w, div_w, csr_w, rs1_valid_w, rs2_valid_w, rd_valid_w, wfi_w, fpu_w, rs1_float_w, rs2_float_w, rs3_float_w, rd_float_w;
// control signals from csr_opt
wire legal_csr_w;
// control signals from priv_opt
wire sysinstr_w;
// 例化 unified_wrapper 及连接代码
decoder_wrapper u_decoder_wrapper (
    .op(op),
    .exec_w          (exec_w),
    .lsu_w           (lsu_w),
    .branch_w        (branch_w),
    .mul_w           (mul_w),
    .div_w           (div_w),
    .csr_w           (csr_w),
    .rs1_valid_w     (rs1_valid_w),
    .rs2_valid_w     (rs2_valid_w),
    .rd_valid_w      (rd_valid_w),
    .wfi_w           (wfi_w),
    .fpu_w           (fpu_w),
    .rs1_float_w     (rs1_float_w),
    .rs2_float_w     (rs2_float_w),
    .rs3_float_w     (rs3_float_w),
    .rd_float_w      (rd_float_w),
    .legal_csr_w     (legal_csr_w),
    .sysinstr_w      (sysinstr_w)
);

/// invalid inst check
wire invalid_w;
wire mul_div_valid_w;
wire rs1_zero_w, rs2_zero_w, rd_zero_w;
wire csr_priv_fault_w;
wire csr_rw_fault_w;

assign rd_zero_w  = (opcode_i[11:7] == 5'b0);
assign rs1_zero_w = (opcode_i[19:15] == 5'b0);
assign rs2_zero_w = (opcode_i[24:20] == 5'b0);
assign mul_div_valid_w = mul_w | div_w;
//csr[9:8] encode the lowest privilege level that can access the CSR.
//00:User, 01:Supervisor, 10: Hypervisor, 11: Machine
assign csr_priv_fault_w = priv_i[1:0] < opcode_i[29:28];
//csr[11:10] encode read/write, write rdonly raise illegal instruction
//11: readonly, other is read/write
assign csr_rw_fault_w = ~((((opcode_i & `INST_CSRRS_MASK) == `INST_CSRRS) |
						((opcode_i & `INST_CSRRC_MASK) == `INST_CSRRC) |
						((opcode_i & `INST_CSRRSI_MASK) == `INST_CSRRSI) |
						((opcode_i & `INST_CSRRCI_MASK) == `INST_CSRRCI)
						) & (opcode_i[19:15] == 5'b0)
				) & (opcode_i[31:30] == 2'b11);
assign invalid_w = valid_i & (~(exec_w | lsu_w | branch_w | mul_div_valid_w | csr_w | sysinstr_w) | (csr_w & (~legal_csr_w | csr_priv_fault_w | csr_rw_fault_w)));

/// control signals in dec_t
assign dec_o = '{
rs1: rs1_valid_w & ~rs1_zero_w,
			 rs2: rs2_valid_w & ~rs2_zero_w,
			 rd: rd_valid_w & ~rd_zero_w,
			 alu_t: exec_w,
			 lsu_t: lsu_w,
			 mul_t: mul_w,
			 div_t: div_w,
			 csr_t: csr_w | invalid_w | fetch_fault_i | wfi_w | sysinstr_w,
			 wfi_t: wfi_w,
			 br_t: branch_w,
			 illegal_t: invalid_w
};

/// other control signals
wire br_w;
wire jal_w;
wire jalr_w;

assign branch_w = br_w | jal_w | jalr_w;
assign br_w = (!op[13]&op[6]&op[5]&!op[4]&!op[3]&!op[2]&op[1]&op[0]) | (op[14]
				&op[6]&op[5]&!op[4]&!op[3]&!op[2]&op[1]&op[0]);
assign jal_w = (op[6]&op[5]&!op[4]&op[3]&op[2]&op[1]&op[0]);
assign jalr_w = (!op[14]&!op[13]&!op[12]&op[6]&op[5]&!op[4]&!op[3]&op[2]&op[1]
				&op[0]);

assign instr_br_o   = br_w;
assign instr_call_o = (jal_w & (op[11:7] == 5'h1 || op[11:7] == 5'h5)) | (jalr_w & (op[11:7] == 5'h1 || (op[11:7] == 5'h5)));
assign instr_ret_o  = jalr_w & (op[19:15] == 5'h1 || op[19:15] == 5'h5) & (op[11:7] != op[19:15]);
assign instr_jmp_o  = (jal_w & (~(op[11:7] == 5'h1 || op[11:7] == 5'h5))) | (jalr_w & (~(op[11:7] == 5'h1 || op[11:7] == 5'h5)));


endmodule
