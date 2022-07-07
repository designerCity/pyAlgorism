n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    
    avg = sum(scores[1:]) / scores[0]
    person = 0
    for j in scores[1:]:
        if j > avg:
            person += 1
    
    rate = person / scores[0] * 100
    print(f'{rate:.3f}%')
# 내가 처음에 적은 답안 : 마지막 리스트에 대해서 계산값이 나오지 않는다.
# 왜인지를 모르겠네
n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    person = 0
    for j in scores[1:]:
        if j > avg:
            person += 1
    
    percent = round(person / scores[0] * 100, 3)
    print(str(percent)+'%' )
