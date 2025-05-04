module tensaurus #(
    parameter MEMORY_ADDRESS_SIZE = 10,
    parameter INDEX_SIZE = 8
) (
    input wire clk,
    input wire rst,

    input wire [MEMORY_ADDRESS_SIZE-1:0] nnz_addr,
    input wire [INDEX_SIZE-1:0] i_or_j,
    input wire [INDEX_SIZE-1:0] k,

    output logic [INDEX_SIZE-1:0] i_index,
    output logic [INDEX_SIZE-1:0] j_index,
    output logic [INDEX_SIZE-1:0] k_index,
    output logic [MEMORY_ADDRESS_SIZE-1:0] nnz_addr_out,
    output logic out_data_valid
);

  logic [INDEX_SIZE-1:0] i_index_temp;
  logic [INDEX_SIZE-1:0] j_index_temp;
  logic [INDEX_SIZE-1:0] k_index_temp;
  logic [MEMORY_ADDRESS_SIZE-1:0] nnz_addr_temp;
  logic temp_valid;

  always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
      i_index_temp  <= '0;
      j_index_temp  <= '0;
      k_index_temp  <= '0;
      nnz_addr_temp <= '0;
      temp_valid    <= 1'b0;
    end else begin
      if (nnz_addr == 0) begin
        i_index_temp <= i_or_j;
        temp_valid   <= 1'b0;
      end else begin
        j_index_temp  <= i_or_j;
        k_index_temp  <= k;
        nnz_addr_temp <= nnz_addr;
        temp_valid    <= 1'b1;
      end
    end
  end

  always_comb begin
    i_index        = i_index_temp;
    j_index        = j_index_temp;
    k_index        = k_index_temp;
    nnz_addr_out   = nnz_addr_temp;
    out_data_valid = temp_valid;
  end

endmodule
