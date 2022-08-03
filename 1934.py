from math import gcd
t = int(input())

def lcm(x, y):
    return x * y // gcd(x, y)

for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))