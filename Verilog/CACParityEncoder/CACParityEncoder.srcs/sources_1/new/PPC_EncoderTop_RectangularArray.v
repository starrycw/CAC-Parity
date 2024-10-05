`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/10/05 16:12:18
// Design Name: 
// Module Name: PPC_EncoderTop_RectangularArray
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


module PPC_EncoderTop_RectangularArray(
    clk, rst_n, data_in, array_out_data, array_out_parityCol, array_out_parityRow
    );

    parameter ARRAYSIZE_nROW = 16;
    parameter ARRAYSIZE_nCOL = 16;
    parameter ARRAYSIZE_bBit = ARRAYSIZE_nROW * ARRAYSIZE_nCOL;

    input wire clk, rst_n;
    input wire [ARRAYSIZE_bBit - 1 : 0] data_in;
    output reg [ARRAYSIZE_bBit - 1 : 0] array_out_data;
    output reg [ARRAYSIZE_nROW - 1 : 0] array_out_parityCol;
    output reg [ARRAYSIZE_nCOL : 0] array_out_parityRow;

    wire [ARRAYSIZE_bBit - 1 : 0] data_in_tr;
    wire [ARRAYSIZE_nROW - 1 : 0] array_out_parityCol_wire;
    wire [ARRAYSIZE_nCOL : 0] array_out_parityRow_wire;

    genvar row_k, col_k;
    generate
        for (row_k = 0; row_k < ARRAYSIZE_nROW - 1; row_k = row_k + 1) begin
            for (col_k = 0; col_k < ARRAYSIZE_nCOL - 1; col_k = col_k + 1) begin
                assign data_in_tr[(col_k * ARRAYSIZE_nROW) + row_k] = data_in[(row_k * ARRAYSIZE_nCOL) + col_k];
            end
        end
    endgenerate

    genvar row_i;
    generate
        for (row_i = 0; row_i < ARRAYSIZE_nROW - 1; row_i = row_i + 1) begin
            PPC_EncoderCore #(.SEQ_LEN(ARRAYSIZE_nCOL)) 
                rowEncoder_instance (
                    .seq_in(data_in[(row_i * ARRAYSIZE_nCOL) + ARRAYSIZE_nCOL - 1 : (row_i * ARRAYSIZE_nCOL)]), 
                    .parity_out(array_out_parityCol_wire[row_i]));
        end
    endgenerate

    genvar col_i;
    generate
        for (col_i = 0; col_i < ARRAYSIZE_nCOL - 1; col_i = col_i + 1) begin
            PPC_EncoderCore #(.SEQ_LEN(ARRAYSIZE_nROW)) 
                colEncoder_instance (
                    .seq_in(data_in_tr[(col_i * ARRAYSIZE_nROW) + ARRAYSIZE_nROW - 1 : (col_i * ARRAYSIZE_nROW)]), 
                    .parity_out(array_out_parityRow_wire[col_i]));
        end
    endgenerate

    assign array_out_parityRow_wire[ARRAYSIZE_nCOL] = ^(array_out_parityRow_wire[ARRAYSIZE_nCOL - 1 : 0]);

    always @(posedge clk or negedge rst_n) begin
        if (~rst_n) begin
            array_out_data <= 0;
            array_out_parityCol <= 0;
            array_out_parityRow <= 0;
        end
        else begin
            array_out_data <= data_in;
            array_out_parityCol <= array_out_parityCol_wire;
            array_out_parityRow <= array_out_parityRow_wire;
        end
    end

endmodule
