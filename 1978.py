n =int(input())
numbers = map(int, input().split())

sosu = 0
for num in numbers:
    error = 0
    if num > 1: # 1은 소수가 아니다. 
        for i in range(2, num):
            if num % i == 0: # 나누었을 때 나머지가 없으면, 소수가 아니다.
                error += 1
        if error == 0:
            sosu += 1

print(sosu)


