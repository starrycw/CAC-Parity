`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/25 21:49:39
// Design Name: 
// Module Name: NormalParity_EncoderCore
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module NormalParity_EncoderCore(
    seq_c, seq_d, seq_g
    );
    parameter BITWIDTH_SEQ = 8;
    input wire [BITWIDTH_SEQ - 1 : 0] seq_c;
    input wire [BITWIDTH_SEQ - 1: 0] seq_d;
    output wire [BITWIDTH_SEQ - 1 : 0] seq_g;

    // Step 1
    assign seq_g[BITWIDTH_SEQ - 1 : 0] = seq_c[BITWIDTH_SEQ - 1 : 0] ^ seq_d[BITWIDTH_SEQ - 1 : 0];
    

endmodule
