module morse_microblaze_wrapper
   (clk_in1_0,
    ext_reset_in_0,
    gpio_io_i_0,
    rx_0,
    tx_0);
  input clk_in1_0;
  input ext_reset_in_0;
  input [5:0]gpio_io_i_0;
  input rx_0;
  output tx_0;

  wire clk_in1_0;
  wire ext_reset_in_0;
  wire [5:0]gpio_io_i_0;
  wire rx_0;
  wire tx_0;

  morse_microblaze morse_microblaze_i
       (.clk_in1_0(clk_in1_0),
        .ext_reset_in_0(ext_reset_in_0),
        .gpio_io_i_0(gpio_io_i_0),
        .rx_0(rx_0),
        .tx_0(tx_0));
endmodule
