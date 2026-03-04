// Benchmark "csr_opt" written by ABC on Tue Mar  3 11:08:06 2026

module csr_opt ( 
    \op[31] , \op[30] , \op[29] , \op[28] , \op[27] , \op[26] , \op[25] ,
    \op[24] , \op[23] , \op[22] , \op[21] , \op[20] ,
    legal_csr_w  );
  input  \op[31] , \op[30] , \op[29] , \op[28] , \op[27] , \op[26] ,
    \op[25] , \op[24] , \op[23] , \op[22] , \op[21] , \op[20] ;
  output legal_csr_w;
  wire new_n14, new_n15, new_n16, new_n17, new_n18, new_n19, new_n20,
    new_n21, new_n22, new_n23, new_n24, new_n25, new_n26, new_n27, new_n28,
    new_n29, new_n30, new_n31, new_n32, new_n33, new_n34, new_n35, new_n36,
    new_n37, new_n38, new_n39, new_n40, new_n41, new_n42, new_n43, new_n44,
    new_n45, new_n46, new_n47, new_n48, new_n49, new_n50, new_n51, new_n52,
    new_n53, new_n54, new_n55, new_n56, new_n57, new_n58, new_n59, new_n60,
    new_n61, new_n62, new_n63, new_n64, new_n65, new_n66, new_n67, new_n68,
    new_n69, new_n70, new_n71, new_n72, new_n73, new_n74, new_n75, new_n76,
    new_n77, new_n78, new_n79, new_n80, new_n81, new_n82, new_n83, new_n84,
    new_n85, new_n86, new_n87, new_n88, new_n89, new_n90, new_n91;
  assign new_n14 = ~\op[31]  & ~\op[30] ;
  assign new_n15 = ~\op[24]  & new_n14;
  assign new_n16 = \op[23]  & \op[21] ;
  assign new_n17 = ~\op[23]  & ~\op[21] ;
  assign new_n18 = ~new_n16 & ~new_n17;
  assign new_n19 = \op[22]  & ~new_n18;
  assign new_n20 = ~\op[22]  & ~new_n16;
  assign new_n21 = ~\op[20]  & ~new_n20;
  assign new_n22 = ~\op[23]  & ~\op[22] ;
  assign new_n23 = \op[23]  & \op[22] ;
  assign new_n24 = ~new_n22 & ~new_n23;
  assign new_n25 = \op[29]  & ~new_n24;
  assign new_n26 = ~new_n19 & ~new_n21;
  assign new_n27 = ~new_n25 & new_n26;
  assign new_n28 = ~\op[27]  & ~new_n27;
  assign new_n29 = ~\op[29]  & ~\op[22] ;
  assign new_n30 = ~\op[20]  & new_n17;
  assign new_n31 = new_n29 & new_n30;
  assign new_n32 = ~new_n28 & ~new_n31;
  assign new_n33 = new_n15 & ~new_n32;
  assign new_n34 = \op[31]  & \op[30] ;
  assign new_n35 = \op[29]  & ~\op[27] ;
  assign new_n36 = ~\op[21]  & ~\op[20] ;
  assign new_n37 = ~\op[22]  & ~new_n36;
  assign new_n38 = \op[22]  & new_n36;
  assign new_n39 = ~new_n37 & ~new_n38;
  assign new_n40 = \op[24]  & ~\op[23] ;
  assign new_n41 = new_n34 & new_n40;
  assign new_n42 = new_n35 & new_n41;
  assign new_n43 = ~new_n39 & new_n42;
  assign new_n44 = ~new_n33 & ~new_n43;
  assign new_n45 = ~\op[25]  & ~new_n44;
  assign new_n46 = new_n15 & new_n35;
  assign new_n47 = \op[27]  & \op[24] ;
  assign new_n48 = new_n34 & new_n47;
  assign new_n49 = ~new_n46 & ~new_n48;
  assign new_n50 = \op[25]  & new_n22;
  assign new_n51 = new_n36 & new_n50;
  assign new_n52 = ~new_n49 & new_n51;
  assign new_n53 = ~new_n45 & ~new_n52;
  assign new_n54 = ~\op[26]  & ~new_n53;
  assign new_n55 = ~\op[20]  & new_n23;
  assign new_n56 = ~new_n22 & ~new_n55;
  assign new_n57 = \op[24]  & ~new_n56;
  assign new_n58 = ~\op[24]  & ~\op[23] ;
  assign new_n59 = \op[22]  & ~\op[20] ;
  assign new_n60 = new_n58 & new_n59;
  assign new_n61 = ~new_n57 & ~new_n60;
  assign new_n62 = ~\op[21]  & ~new_n61;
  assign new_n63 = ~\op[22]  & new_n58;
  assign new_n64 = ~new_n62 & ~new_n63;
  assign new_n65 = \op[26]  & ~new_n64;
  assign new_n66 = ~\op[29]  & ~\op[24] ;
  assign new_n67 = ~\op[21]  & \op[20] ;
  assign new_n68 = new_n66 & new_n67;
  assign new_n69 = new_n23 & new_n68;
  assign new_n70 = ~new_n65 & ~new_n69;
  assign new_n71 = ~\op[30]  & ~\op[27] ;
  assign new_n72 = ~new_n70 & new_n71;
  assign new_n73 = \op[30]  & \op[29] ;
  assign new_n74 = \op[27]  & \op[26] ;
  assign new_n75 = new_n36 & new_n73;
  assign new_n76 = new_n74 & new_n75;
  assign new_n77 = new_n63 & new_n76;
  assign new_n78 = ~new_n72 & ~new_n77;
  assign new_n79 = ~\op[31]  & ~\op[25] ;
  assign new_n80 = ~new_n78 & new_n79;
  assign new_n81 = ~new_n54 & ~new_n80;
  assign new_n82 = \op[28]  & ~new_n81;
  assign new_n83 = new_n14 & ~new_n36;
  assign new_n84 = ~\op[21]  & new_n34;
  assign new_n85 = ~new_n83 & ~new_n84;
  assign new_n86 = ~\op[28]  & ~\op[27] ;
  assign new_n87 = ~\op[26]  & ~\op[25] ;
  assign new_n88 = new_n86 & new_n87;
  assign new_n89 = new_n29 & new_n58;
  assign new_n90 = new_n88 & new_n89;
  assign new_n91 = ~new_n85 & new_n90;
  assign legal_csr_w = new_n82 | new_n91;
endmodule


