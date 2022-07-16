n = int(input())

num = 2 # 나누는 수
while n != 1:
    if n % num == 0: # 나누어 떨어지는 경우
        print(num)
        n = n // num
        # print(n)
    else:
        num += 1