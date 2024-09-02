`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/09/02 14:27:25
// Design Name: 
// Module Name: OED_ErrorCounter
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


module OED_ErrorCounter(
    clk, rst_n, flag_error, flag_bist
    );

    parameter TH_ERRORCNT = 8;
    parameter BITWIDTH_ERRORCNT = 3;
    
    input wire clk, rst_n, flag_error;
    output reg flag_bist;
    
    // cnt
    reg [BITWIDTH_ERRORCNT - 1 : 0] errorcnt;

    wire flag_bist_wire;
    assign flag_bist_wire = (errorcnt == TH_ERRORCNT)? 1'b1 : 1'b0;

    always @(posedge clk or negedge rst_n) begin
        if (~rst_n) begin
            errorcnt <= 0;
            flag_bist <= 1'b0;
        end
        else begin
            errorcnt <= errorcnt + ((~flag_bist_wire) & flag_error);
            flag_bist <= flag_bist_wire;
        end
    end

endmodule
