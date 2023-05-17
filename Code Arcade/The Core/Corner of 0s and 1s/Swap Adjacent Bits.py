def solution(n):
    return ((n << 1) & 0xaaaaaaaa) | ((n >> 1) & 0x55555555)
