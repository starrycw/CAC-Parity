`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/09/02 15:21:29
// Design Name: 
// Module Name: OED_ParityCmpCore
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


module OED_ParityCmpCore(
    seq_a, seq_b, flag_error
    );

    parameter BITWIDTH_SEQ = 8;

    input wire [BITWIDTH_SEQ - 1 : 0] seq_a;
    input wire [BITWIDTH_SEQ - 1 : 0] seq_b;
    output wire flag_error;

    // cmp core
    assign flag_error = (seq_a == seq_b) ? (1'b0) : (1'b1);


endmodule
