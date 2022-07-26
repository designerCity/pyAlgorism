# 356 ms 걸린 내 코드
import sys
a, b = map(int, input().split())
input = sys.stdin.readline

pocket_li = []
# input 받기
# for _ in range(a):
#     pocket_li.append(input().rstrip()) # .rstrip 을 사용하면 문자열의 \n 을 제거할 수 있다.
pocket_li =[input().rstrip() for i in range(a)]
srch_li = dict() # 사전

# 사전에 번호 메기기
for i in range(a):
    srch_li[pocket_li[i]] = str(i+1)

reverde_srch = dict(map(reversed, srch_li.items()))
# 탐색
for i in range(b):
    tgt = input().rstrip()
    if tgt.isdigit(): # .isdigit()은 True / False 를 return 한다.
        print(reverde_srch[tgt])
    else:
        print(srch_li[tgt])



# 280 ms 걸린 다른 사람 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
# 이 코드에서는 for 문을 통해 key-value 와 value-key 두 쌍을 저장해두고 사용한 점이 인상적이다.
for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
