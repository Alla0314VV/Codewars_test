from operator import mul
from functools import reduce

def going(n, k=7):
    denominator = [reduce(mul, [n - j for j in range(i+1)]) for i in range(k) if i != n-1]
    return int((1 + sum(map(lambda x: 1/x if x != 0 else 0, denominator)))*1e6)/1e6
