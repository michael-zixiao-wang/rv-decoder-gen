// Benchmark "priv_opt" written by ABC on Tue Mar  3 11:08:06 2026

module priv_opt ( 
    \op[31] , \op[30] , \op[29] , \op[28] , \op[27] , \op[26] , \op[25] ,
    \op[24] , \op[23] , \op[22] , \op[21] , \op[20] , \op[19] , \op[18] ,
    \op[17] , \op[16] , \op[15] , \op[14] , \op[13] , \op[12] , \op[11] ,
    \op[10] , \op[9] , \op[8] , \op[7] , \op[6] , \op[5] , \op[4] ,
    \op[3] , \op[2] , \op[1] , \op[0] ,
    sysinstr_w  );
  input  \op[31] , \op[30] , \op[29] , \op[28] , \op[27] , \op[26] ,
    \op[25] , \op[24] , \op[23] , \op[22] , \op[21] , \op[20] , \op[19] ,
    \op[18] , \op[17] , \op[16] , \op[15] , \op[14] , \op[13] , \op[12] ,
    \op[11] , \op[10] , \op[9] , \op[8] , \op[7] , \op[6] , \op[5] ,
    \op[4] , \op[3] , \op[2] , \op[1] , \op[0] ;
  output sysinstr_w;
  wire new_n34, new_n35, new_n36, new_n37, new_n38, new_n39, new_n40,
    new_n41, new_n42, new_n43, new_n44, new_n45, new_n46, new_n47, new_n48,
    new_n49, new_n50, new_n51, new_n52, new_n53, new_n54, new_n55, new_n56,
    new_n57, new_n58, new_n59, new_n60, new_n61, new_n62, new_n63, new_n64,
    new_n65, new_n66, new_n67, new_n68, new_n69, new_n70, new_n71, new_n72,
    new_n73, new_n74, new_n75, new_n76;
  assign new_n34 = \op[28]  & \op[20] ;
  assign new_n35 = \op[22]  & ~new_n34;
  assign new_n36 = \op[28]  & ~\op[22] ;
  assign new_n37 = ~\op[29]  & ~\op[21] ;
  assign new_n38 = ~new_n36 & new_n37;
  assign new_n39 = ~new_n35 & new_n38;
  assign new_n40 = \op[21]  & ~\op[20] ;
  assign new_n41 = new_n36 & new_n40;
  assign new_n42 = ~new_n39 & ~new_n41;
  assign new_n43 = ~\op[25]  & ~\op[24] ;
  assign new_n44 = ~\op[23]  & ~\op[19] ;
  assign new_n45 = ~\op[18]  & ~\op[17] ;
  assign new_n46 = ~\op[16]  & ~\op[15] ;
  assign new_n47 = new_n45 & new_n46;
  assign new_n48 = new_n43 & new_n44;
  assign new_n49 = new_n47 & new_n48;
  assign new_n50 = ~new_n42 & new_n49;
  assign new_n51 = ~\op[29]  & \op[28] ;
  assign new_n52 = \op[25]  & new_n51;
  assign new_n53 = ~new_n50 & ~new_n52;
  assign new_n54 = ~\op[31]  & ~\op[30] ;
  assign new_n55 = ~\op[27]  & ~\op[26] ;
  assign new_n56 = ~\op[12]  & ~\op[11] ;
  assign new_n57 = ~\op[10]  & ~\op[9] ;
  assign new_n58 = ~\op[8]  & ~\op[7] ;
  assign new_n59 = \op[6]  & \op[5] ;
  assign new_n60 = \op[4]  & ~\op[3] ;
  assign new_n61 = ~\op[2]  & new_n60;
  assign new_n62 = new_n58 & new_n59;
  assign new_n63 = new_n56 & new_n57;
  assign new_n64 = new_n54 & new_n55;
  assign new_n65 = new_n63 & new_n64;
  assign new_n66 = new_n61 & new_n62;
  assign new_n67 = new_n65 & new_n66;
  assign new_n68 = ~new_n53 & new_n67;
  assign new_n69 = ~\op[6]  & ~\op[5] ;
  assign new_n70 = ~\op[4]  & \op[3] ;
  assign new_n71 = \op[2]  & new_n70;
  assign new_n72 = new_n69 & new_n71;
  assign new_n73 = ~new_n68 & ~new_n72;
  assign new_n74 = ~\op[14]  & ~\op[13] ;
  assign new_n75 = \op[1]  & \op[0] ;
  assign new_n76 = new_n74 & new_n75;
  assign sysinstr_w = ~new_n73 & new_n76;
endmodule


