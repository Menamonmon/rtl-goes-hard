`timescale		    1ns/1ps
`default_nettype    none

module tailors #
  (
    parameter BUFFER_SIZE = 4,
    parameter WORD_SIZE = 4)
  (
    input wire clk, 
    input wire rst,

    input wire [WORD_SIZE-1:0] a_input,
    input wire a_input_valid,

    input wire [WORD_SIZE-1:0] b_input,
    input wire b_input_valid,

    input wire new_row,

    output logic [WORD_SIZE-1:0] mul1,
    output logic [WORD_SIZE-1:0] mul2,
    output logic out_data_valid
  );


  logic [WORD_SIZE-1:0][BUFFER_SIZE-1:0] a_buf;
  logic [BUFFER_SIZE-1:0] a_buf_valid;
  logic [$clog2(BUFFER_SIZE+1)-1:0] a_buf_length;

  logic [WORD_SIZE-1:0][BUFFER_SIZE-1:0] b_buf;
  logic [BUFFER_SIZE-1:0] b_buf_valid;
  logic [$clog2(BUFFER_SIZE+1)-1:0] b_buf_length;


  assign mul1 = a_buf[a_buf_length];
  assign mul2 = b_buf[a_buf_length];


  always_ff @(posedge clk) begin

    if (rst || new_row) begin
        a_buf <= 0;
        a_buf_valid <= 0;
        b_buf <= 0;
        b_buf_valid <= 0;

        a_buf_length <= 0;
        b_buf_length <= 0;
        out_data_valid <= 0;
    end

    else begin

      if (a_input_valid) begin
        a_buf[a_buf_length] <= a_input;
        a_buf_valid[a_buf_length] <= 1;
        a_buf_length <= a_buf_length == BUFFER_SIZE-1 ? a_buf_length : a_buf_length + 1;
      end

      if (b_input_valid) begin
        b_buf[b_buf_length] <= b_input;
        b_buf_valid[b_buf_length] <= 1;
        b_buf_length <= b_buf_length == BUFFER_SIZE-1 ? b_buf_length : b_buf_length + 1;
      end

      out_data_valid <= a_input_valid || b_input_valid;

    end
  end
endmodule