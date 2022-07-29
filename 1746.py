# # 시간 초과
# a, b = map(int, input().split())

# know_li = []
# for i in range(a):
#     know_li.append(input())

# srch_li = []
# for i in range(b):
#     srch_li.append(input())

# result = []
# for i in know_li:
#     if i in srch_li:
#         result.append(i)
        
# result.sort()
# print(len(result))
# for i in result:
#     print(i)

# 참고한 풀이 list 를 사용하지 않는 set
a, b = map(int, input().split())

set1 = set()
for i in range(a):
    set1.add(input())

set2 = set()
for i in range(b):
    set2.add(input())

result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)

# 다른 방법
import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)