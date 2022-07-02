# 입력이 여러 값일 때
while 1:
    a,b = map(int, input().split())
    # 빈칸일때 0 처리 받을 수 있다.
    if (a == 0 and b == 0):
        break
    else:
        print(a + b)
