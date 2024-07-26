`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/23 15:55:44
// Design Name: 
// Module Name: FTFParity_EncoderCore
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


module FTFParity_EncoderCore(
    seq_c, seq_d, seq_g
    );
    parameter BITWIDTH_SEQ = 8;
    input wire [BITWIDTH_SEQ - 1 : 0] seq_c;
    input wire [BITWIDTH_SEQ - 1: 0] seq_d;
    output wire [BITWIDTH_SEQ - 1 : 0] seq_g;

    // Step 1
    wire [BITWIDTH_SEQ - 1: 0] seq_e;
    genvar e_i;
    generate for (e_i = 0; e_i < BITWIDTH_SEQ; e_i = e_i + 2) begin
        assign seq_e[e_i] = seq_c[e_i] ^ seq_d[e_i];
    end
    endgenerate

    genvar e_j;
    generate for (e_j = 1; e_j < BITWIDTH_SEQ; e_j = e_j + 2) begin
        assign seq_e[e_j] = seq_c[e_j] ~^ seq_d[e_j];
    end
    endgenerate

    // Step 2
    wire [BITWIDTH_SEQ - 1:0] seq_f;
    genvar f_i;
    generate for (f_i = 0; f_i < BITWIDTH_SEQ - 1; f_i = f_i + 2) begin
        assign seq_f[f_i] = ( (seq_e[f_i] == 1'b0) & (seq_e[f_i + 1] == 1'b1) )? (seq_c[f_i]) : (seq_e[f_i]);
        assign seq_f[f_i + 1] = ( (seq_e[f_i] == 1'b0) & (seq_e[f_i + 1] == 1'b1) )? (seq_c[f_i + 1]) : (seq_e[f_i + 1]);
    end
    endgenerate

    generate if ( (BITWIDTH_SEQ % 2) == 1) begin
        assign seq_f[BITWIDTH_SEQ - 1] = seq_e[BITWIDTH_SEQ - 1];
    end
    endgenerate

    // Step 3
    // wire [BITWIDTH_SEQ - 1:0] seq_g;
    genvar g_i;
    generate for (g_i = 1; g_i < BITWIDTH_SEQ - 1; g_i = g_i + 2) begin
        assign seq_g[g_i] = ( (seq_f[g_i] == 1'b1) & (seq_f[g_i + 1] == 1'b0) )? (seq_c[g_i]) : (seq_f[g_i]);
        assign seq_g[g_i + 1] = ( (seq_f[g_i] == 1'b1) & (seq_f[g_i + 1] == 1'b0) )? (seq_c[g_i + 1]) : (seq_f[g_i + 1]);
    end
    endgenerate

    generate if ( (BITWIDTH_SEQ % 2) == 0) begin
        assign seq_g[BITWIDTH_SEQ - 1] = seq_f[BITWIDTH_SEQ - 1];
    end
    endgenerate

    assign seq_g[0] = seq_f[0];
    

endmodule
