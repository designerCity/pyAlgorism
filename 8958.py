n = int(input())

for i in range(n):
    ox_list = list(input())
    
    total = 0
    score = 0 # 점수 누적되는 변수
    # 받은 리스트 탐색하는 반복문
    
    for ox in ox_list:
        if ox == 'O':
            score += 1
            total += score
        else:
            score = 0            
    print(total)