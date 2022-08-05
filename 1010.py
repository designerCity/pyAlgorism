t = int(input()) # test 개수

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for i in range(t):
    a, b = map(int, input().split())
    print(round(factorial(b) / (factorial(b-a) * factorial(a))))