n = int(input())

def fibonach(n):
    if n <= 1:
        return n
    return fibonach(n-1) + fibonach(n-2)

print(fibonach(n))