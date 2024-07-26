`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/23 21:10:50
// Design Name: 
// Module Name: tb_FPFParity_EncoderTop
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


module tb_FPFParity_EncoderTop(

    );
    
    parameter BITWIDTH_SEQ = 27;
    `define DEF_BITWIDTH 27
    
    // DUT
    reg [BITWIDTH_SEQ - 1 : 0] seq_a, seq_b, seq_a_reverse;
    reg clk, state_ctrl;
    
    FPFParity_EncoderTop #(.BITWIDTH_SEQ(BITWIDTH_SEQ)) enc01(
        .clk(clk),
        .state_ctrl(state_ctrl), 
        .seq_a(seq_a_reverse),
        .seq_b(seq_b)
    );
    
    // Reverse
    genvar r_i;
    generate
        for (r_i = 0; r_i < BITWIDTH_SEQ; r_i = r_i + 1) begin
            always @ (*) begin
                seq_a_reverse[r_i] <= seq_a[BITWIDTH_SEQ - r_i - 1];
            end
        end
    endgenerate
    
    
    // Simu
    initial begin:simu_main
        clk = 1'b0;
        state_ctrl = 1'b1;
        seq_a = `DEF_BITWIDTH'b0_1_1_1_1_0_0_0_0_1_1_0_0_1_1_0_0_0_0_0_0_1_1_1_1_0_0;
        #1;
        clk = 1'b1;

        #1;
        clk = 1'b0;
        state_ctrl = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_0_0_0_0_0_0_0_0_0_1_1_1_0_0_0_1_1_0_0_1_1_0_0_0_1_1;
        #1;
        clk = 1'b1;
  
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_1_1_0_0_1_1_1_0_0_0_0_0_1_1_0_0_1_1_0_0_1_1_1_1_0_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_1_0_0_1_1_0_0_1_1_1_1_1_0_0_1_1_1_1_0_0_0_1_1_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_0_0_0_1_1_1_0_0_0_1_1_1_1_0_0_1_1_0_0_1_1_0_0_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_1_1_0_0_1_1_0_0_1_1_1_0_0_1_1_1_1_1_1_1_1_1_0_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_0_0_0_1_1_1_1_1_0_0_0_0_1_1_1_0_0_0_0_1_1_1_1_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_0_0_1_1_0_0_1_1_1_1_1_0_0_1_1_1_0_0_0_0_0_1_1_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_0_1_1_0_0_0_1_1_1_0_0_1_1_0_0_1_1_1_1_1_0_0_0_0_0_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_0_0_0_0_1_1_1_0_0_1_1_1_0_0_1_1_1_1_0_0_1_1_1_1_1_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_0_1_1_1_0_0_0_0_0_1_1_1_1_1_0_0_1_1_1_0_0_0_1_1_1_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_1_1_0_0_0_1_1_1_1_0_0_0_1_1_1_1_1_0_0_0_0_0_0_0_0_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_0_0_0_0_1_1_1_0_0_1_1_0_0_1_1_0_0_0_0_1_1_0_0_1_1_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b0_0_0_1_1_0_0_0_1_1_1_1_1_0_0_0_0_1_1_0_0_0_1_1_0_0_1;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_1_0_0_0_1_1_0_0_1_1_1_1_1_1_1_1_0_0_0_0_1_1_1_0_0_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        seq_a = `DEF_BITWIDTH'b1_1_0_0_1_1_1_0_0_1_1_1_0_0_1_1_0_0_1_1_0_0_1_1_1_0_0;
        #1;
        clk = 1'b1;
        #1;
        clk = 1'b0;
        $display("Result: %b", seq_b);
        state_ctrl = 1'b1;
        #1; 
        $finish();
    end:simu_main
    
    
    
endmodule
