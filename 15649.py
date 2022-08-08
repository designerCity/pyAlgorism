# # 정답 풀이
n, m = map(int, input().split())

s = []
def cbt():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return 
  for i in range(1, n + 1):
    if i in s:
      continue # s 안에 i 가 있을 때 i 를 추가하는 것을 넘어간다. 
    s.append(i)
    cbt()   # 이 코드에서 아래로 내려가면 출력을 마친 상태이다.
    s.pop() # pop 으로 list 맨 마지막 요소를 돌려주고 그 요소를 삭제한다. 이를 통해 대체 가능해진다. 

cbt()


# # 다른 사람 코드
# def sol(index, n, m) :
    
#     if index == m :
#         print(' '.join(map(str, answer)))
#         return
    
#     for i in range(1, n+1) :
#         if check[i] == True :
#             continue
        
#         check[i] = True
#         answer[index] = i
#         sol(index+1, n, m)
#         check[i] = False
        
# ##########
# n, m = map(int, input().split())
# check = [False] * (n+1)
# answer = [0] * m

# sol(0, n, m)