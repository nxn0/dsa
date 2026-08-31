int reverseBits(int n) {
    for (size_t c = sizeof n * CHAR_BIT, r = 0, z = n ; --c || (n = r, 0) ; r = (r | z & 1) << 1, z >>= 1);
    return n;
}