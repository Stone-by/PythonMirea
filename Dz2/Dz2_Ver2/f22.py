def f22(x):
    a_bits = 0b00000000000000000000000011111111
    b_bits = 0b00000000000111111111111100000000
    c_bits = 0b00000001111000000000000000000000
    d_bits = 0b01111110000000000000000000000000
    e_bits = 0b10000000000000000000000000000000
    new_a_bits = (x & a_bits) << 5
    new_b_bits = (x & b_bits) << 5
    new_c_bits = (x & c_bits) >> 20
    new_d_bits = (x & d_bits) << 1
    new_e_bits = (x & e_bits) >> 31
    return new_a_bits | new_b_bits | new_c_bits | new_d_bits | new_e_bits

x = 0x3799ec28
f22(x)