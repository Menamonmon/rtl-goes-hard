`timescale		    1ns/1ps
`default_nettype    none

module highlight #
  ( 
    parameter WORD_SIZE = 8)
  (
    input wire clk, 
    input wire rst,

    input wire [3:0] [3:0] [WORD_SIZE-1:0] blocks,
    input wire [1:0] [1:0] block_selector,
    input wire blocks_valid_in,

    input wire [1:0] [1:0] [1:0] word_selector,

    output logic [3:0] [WORD_SIZE-1:0] words_out,
    output logic words_valid_out
  );


  logic [1:0] [3:0] [WORD_SIZE-1:0] stored_blocks;
  logic stored_blocks_valid;


  always_ff @(posedge clk) begin

    if (rst) begin
        words_out <= 0;
        words_valid_out <= 0;
        stored_blocks <= 0;
        stored_blocks_valid <= 0;
    end

    else begin

      if (blocks_valid_in) begin
        stored_blocks[0] <= blocks[word_selector[0]];
        stored_blocks[1] <= blocks[word_selector[1]];
        stored_blocks_valid <= 1;
      end

      else begin
        stored_blocks_valid <= 0;
      end


      if (stored_blocks_valid) begin
        words_out[0][0] <= stored_blocks[word_selector[0][0]];
        words_out[0][1] <= stored_blocks[word_selector[0][1]];

        words_out[1][0] <= stored_blocks[word_selector[1][0]];
        words_out[1][1] <= stored_blocks[word_selector[1][1]];
         
        words_valid_out <= 1;
      end

      else begin
        words_valid_out <= 0;
      end
    end
  end
endmodule