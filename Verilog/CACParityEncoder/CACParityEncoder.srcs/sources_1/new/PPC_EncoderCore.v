`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/10/05 22:17:30
// Design Name: 
// Module Name: PPC_EncoderCore
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


module PPC_EncoderCore(
    seq_in, parity_out
    );

    parameter SEQ_LEN = 16;

    input [SEQ_LEN - 1 : 0] seq_in;
    output parity_out;

    assign parity_out = ^(seq_in);


endmodule
