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
