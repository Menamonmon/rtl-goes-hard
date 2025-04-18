`timescale		    1ns/1ps
`default_nettype    none

module NVIDIA #
  (
    parameter BLOCK_SIZE = 4,
    parameter NUM_SELECT = 3,
    parameter WORD_SIZE = 8)
  (
    input wire clk, 
    input wire rst,

    input wire [WORD_SIZE-1:0][NUM_SELECT-1:0] a,
    input wire [WORD_SIZE-1:0][BLOCK_SIZE-1:0] b,
    input wire [$clog2(NUM_SELECT+1)-1:0][NUM_SELECT-1:0] b_selectors,
    output logic [WORD_SIZE-1:0][NUM_SELECT-1:0] out
  );




  always_ff @(posedge clk) begin

    if (rst) begin
        out <= 0;
    end

    else begin
      for (int i = 0; i < NUM_SELECT; i = i + 1) begin
        out[i] <= b[b_selectors[i]];
      end
    end
  end
endmodule