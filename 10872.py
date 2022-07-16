n = int(input())

def factorial(n):
    fac_num = 1
    
    if n > 1:
        fac_num = n * factorial(n-1)
    return fac_num

print(factorial(n))

# def factorial(n):
#     if n>1: return n*factorial(n-1)
#     else: return 1
    
# print(factorial(int(input())))