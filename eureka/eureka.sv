module eureka #(
    parameter WIDTH = 32,     // Width of each input element (bits)
    parameter NUM_INPUTS = 32 // Number of input elements
) (
    input logic [WIDTH-1:0] input_matrix[NUM_INPUTS-1:0],  // Input matrix
    output logic [WIDTH-1:0] data_out[NUM_INPUTS-1:0],  // Compacted data
    output logic [$clog2(NUM_INPUTS)-1:0] addr_out[NUM_INPUTS-1:0],  // Original indices
    output logic [$clog2(NUM_INPUTS):0] num_valid  // Number of valid (nonzero) outputs
);

  // Internal signals
  logic is_nonzero[NUM_INPUTS-1:0];
  logic [$clog2(NUM_INPUTS):0] prefix_sum[NUM_INPUTS:0];

  integer i;

  // Step 1: Detect nonzeros
  always_comb begin
    for (i = 0; i < NUM_INPUTS; i = i + 1) begin
      is_nonzero[i] = (input_matrix[i] != 0);
    end
  end

  // Step 2: Compute prefix sum (serial scan, can be parallelized if needed)
  always_comb begin
    prefix_sum[0] = 0;
    for (i = 0; i < NUM_INPUTS; i = i + 1) begin
      prefix_sum[i+1] = prefix_sum[i] + is_nonzero[i];
    end
  end

  // Step 3: Compact data and generate addresses
  always_comb begin
    // Default outputs
    for (i = 0; i < NUM_INPUTS; i = i + 1) begin
      data_out[i] = '0;
      addr_out[i] = '0;
    end

    for (i = 0; i < NUM_INPUTS; i = i + 1) begin
      if (is_nonzero[i]) begin
        data_out[prefix_sum[i]] = input_matrix[i];
        addr_out[prefix_sum[i]] = i[$clog2(NUM_INPUTS)-1:0];
      end
    end

    num_valid = prefix_sum[NUM_INPUTS];
  end

endmodule
