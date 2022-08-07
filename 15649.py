# # 정답 풀이
n, m = map(int, input().split())

s = []
def cbt():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return 
  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    cbt()   # 이 코드에서 아래로 내려가면 출력을 마친 상태이다.
    s.pop() # pop 으로 list 맨 마지막 요소를 돌려주고 그 요소를 삭제한다. 이를 통해 대체 가능해진다. 

cbt()