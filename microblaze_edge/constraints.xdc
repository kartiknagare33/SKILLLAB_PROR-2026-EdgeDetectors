# -------------------------------------------------------------------------
# 1. GPIO: Button (Bit 0) PMOD Mic (Bit 1) change to mic (bit 2)  reset (bit 3) change to encode (bit 4) hex input from pmod (bit 5)
# -------------------------------------------------------------------------
set_property -dict {PACKAGE_PIN J2 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[0]}] 
set_property -dict {PACKAGE_PIN A14 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[1]}] 
set_property -dict {PACKAGE_PIN V2 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[2]}]
set_property -dict {PACKAGE_PIN J5 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[3]}]
set_property -dict {PACKAGE_PIN U2 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[4]}]
set_property -dict {PACKAGE_PIN B14 IOSTANDARD LVCMOS33} [get_ports {gpio_io_i_0[5]}]

# -------------------------------------------------------------------------
# 2. UART: RX and TX for Vitis Terminal
# -------------------------------------------------------------------------
set_property -dict {PACKAGE_PIN V12 IOSTANDARD LVCMOS33} [get_ports {rx_0}]
set_property -dict {PACKAGE_PIN U11 IOSTANDARD LVCMOS33} [get_ports {tx_0}]

# -------------------------------------------------------------------------
# 3. RESET: Tied to On-board Button 3 (btn[3])
# -------------------------------------------------------------------------
set_property -dict {PACKAGE_PIN J1 IOSTANDARD LVCMOS33} [get_ports {ext_reset_in_0}]

# -------------------------------------------------------------------------
# 4. CLOCK: Single-ended pin tied to F14 (100MHz Oscillator)
# -------------------------------------------------------------------------
set_property -dict {PACKAGE_PIN F14 IOSTANDARD LVCMOS33} [get_ports {clk_in1_0}]
create_clock -period 10.000 -name gclk [get_ports {clk_in1_0}]
