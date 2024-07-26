`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/23 20:10:44
// Design Name: 
// Module Name: FTFParity_EncoderTop
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


module FTFParity_EncoderTop(
    clk, state_ctrl, seq_a, seq_b
    );

    parameter BITWIDTH_SEQ = 8;

    input wire clk;
    input wire state_ctrl; // 0 - Data seq in (normal); 1 - Read out parity seq (reset parity reg when the clk posedge detected).
    input wire [BITWIDTH_SEQ - 1 : 0] seq_a;
    output reg [BITWIDTH_SEQ - 1 : 0] seq_b;

    // Encoder_core
    wire [BITWIDTH_SEQ - 1 : 0] seq_b_temp;
    FTFParity_EncoderCore #(.BITWIDTH_SEQ(BITWIDTH_SEQ)) enc01 (
        .seq_c(seq_b), 
        .seq_d(seq_a), 
        .seq_g(seq_b_temp)
    );

    // Update regs
    always @(posedge clk) begin
        if (state_ctrl == 1'b0) begin
            seq_b <= seq_b_temp;
        end
        else begin
            seq_b <= seq_a;
        end
    end

endmodule
