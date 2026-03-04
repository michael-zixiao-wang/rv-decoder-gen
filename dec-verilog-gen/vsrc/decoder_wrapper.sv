// Auto-generated Unified Wrapper for ABC synthesized netlists
// Included Modules: dec_opt, csr_opt, priv_opt

module decoder_wrapper (
    input  [31:0] op,
    output exec_w,
    output lsu_w,
    output branch_w,
    output mul_w,
    output div_w,
    output csr_w,
    output rs1_valid_w,
    output rs2_valid_w,
    output rd_valid_w,
    output wfi_w,
    output fpu_w,
    output rs1_float_w,
    output rs2_float_w,
    output rs3_float_w,
    output rd_float_w,
    output legal_csr_w,
    output sysinstr_w
);

    // ---------------------------------------------------------
    // inst dec_opt 
    // ---------------------------------------------------------
    \dec_opt  u_dec_opt (
        .\op[31]  (op[31]),
        .\op[30]  (op[30]),
        .\op[29]  (op[29]),
        .\op[28]  (op[28]),
        .\op[27]  (op[27]),
        .\op[26]  (op[26]),
        .\op[25]  (op[25]),
        .\op[24]  (op[24]),
        .\op[23]  (op[23]),
        .\op[22]  (op[22]),
        .\op[21]  (op[21]),
        .\op[20]  (op[20]),
        .\op[19]  (op[19]),
        .\op[18]  (op[18]),
        .\op[17]  (op[17]),
        .\op[16]  (op[16]),
        .\op[15]  (op[15]),
        .\op[14]  (op[14]),
        .\op[13]  (op[13]),
        .\op[12]  (op[12]),
        .\op[11]  (op[11]),
        .\op[10]  (op[10]),
        .\op[9]  (op[9]),
        .\op[8]  (op[8]),
        .\op[7]  (op[7]),
        .\op[6]  (op[6]),
        .\op[5]  (op[5]),
        .\op[4]  (op[4]),
        .\op[3]  (op[3]),
        .\op[2]  (op[2]),
        .\op[1]  (op[1]),
        .\op[0]  (op[0]),
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
        .rd_float_w      (rd_float_w)
    );

    // ---------------------------------------------------------
    // inst csr_opt 
    // ---------------------------------------------------------
    \csr_opt  u_csr_opt (
        .\op[31]  (op[31]),
        .\op[30]  (op[30]),
        .\op[29]  (op[29]),
        .\op[28]  (op[28]),
        .\op[27]  (op[27]),
        .\op[26]  (op[26]),
        .\op[25]  (op[25]),
        .\op[24]  (op[24]),
        .\op[23]  (op[23]),
        .\op[22]  (op[22]),
        .\op[21]  (op[21]),
        .\op[20]  (op[20]),
        .legal_csr_w     (legal_csr_w)
    );

    // ---------------------------------------------------------
    // inst priv_opt 
    // ---------------------------------------------------------
    \priv_opt  u_priv_opt (
        .\op[31]  (op[31]),
        .\op[30]  (op[30]),
        .\op[29]  (op[29]),
        .\op[28]  (op[28]),
        .\op[27]  (op[27]),
        .\op[26]  (op[26]),
        .\op[25]  (op[25]),
        .\op[24]  (op[24]),
        .\op[23]  (op[23]),
        .\op[22]  (op[22]),
        .\op[21]  (op[21]),
        .\op[20]  (op[20]),
        .\op[19]  (op[19]),
        .\op[18]  (op[18]),
        .\op[17]  (op[17]),
        .\op[16]  (op[16]),
        .\op[15]  (op[15]),
        .\op[14]  (op[14]),
        .\op[13]  (op[13]),
        .\op[12]  (op[12]),
        .\op[11]  (op[11]),
        .\op[10]  (op[10]),
        .\op[9]  (op[9]),
        .\op[8]  (op[8]),
        .\op[7]  (op[7]),
        .\op[6]  (op[6]),
        .\op[5]  (op[5]),
        .\op[4]  (op[4]),
        .\op[3]  (op[3]),
        .\op[2]  (op[2]),
        .\op[1]  (op[1]),
        .\op[0]  (op[0]),
        .sysinstr_w      (sysinstr_w)
    );

endmodule
