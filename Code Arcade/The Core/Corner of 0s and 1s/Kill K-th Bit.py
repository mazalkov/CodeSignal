def solution(n, k):
    return n & ~(2**(k-1))
