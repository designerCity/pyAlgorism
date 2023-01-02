n = int(input())
li = []
for i in range(n):
    li.append(int(input()))


dp_li = [0] * n # 지금까지의 계단 합
# 동적 프로그래밍은 재귀함수보다 훨씬 빠르게 동작한다.
if len(li) <= 2:
    print(sum(li))
else:
    dp_li[0] = li[0] # 첫째 계단 계산
    dp_li[1] = li[0] + li[1] # 둘째 계단까지 계산

    for i in range(2, n):
        dp_li[i] = max(dp_li[i-3] + li[i-1] +li[i], dp_li[i-2] + li[i]) # 마지막 + 연속 / 띄기

    print(dp_li[n-1])
