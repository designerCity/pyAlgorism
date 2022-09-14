# 파도반 수열
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    case = int(input())
    n = case
    # 나선에서 가장 긴 변의 길이를 k 라고 한다.
    p_li = [1, 1, 1, 2, 2, 3]
    while n > 
    if n > 5:
        p_li.append(p_li[case] + p_li[case - 4])
    else:

    print(p_li[case-1]) # 출력