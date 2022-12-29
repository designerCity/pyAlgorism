import sys

# RGB 거리
input = sys.stdin.readline
h = int(input())
all_case = []

# 조건 각 집이 인접한 집과 색깔이 일치하지 않게 만들기
for _ in range(h):
    all_case.append(list(map(int, sys.stdin.readline().rstrip().split())))
print(all_case)
all_case0 = all_case
all_case1 = all_case
all_case2 = all_case
# li = [1, 2, 1]
# del li[li.index(min(li))]
# print(li[li.index(min(li))])

# 두 번째를 찾기 위한 함수 input 을 li를 받음
def second_min(li):
    min_num = min(li)
    min_index = li.index(min(li))
    # 같은 경우
    for i in range(3):
        if (li[i] == min(li)) and (min_index != i ):
            # del li[li.index(min(li))]
            # second_min_num = li.index(min(li))
            # li.insert(min_index, min_num)
            return i
    # 두 번째 작은 값 찾기
    del li[li.index(min(li))]
    second_min_num = li.index(min(li)) + 1
    li.insert(min_index, min_num)
    return second_min_num # 두 번째로 작은 index 를 출력함. 

value = 0
index_case = []

for i in range(h):    
    case_min = min(all_case[i])
    case_idx = all_case[i].index(case_min)
    # case_idx = second_min(all_case[i])
    if (index_case == []) or index_case[i-1] != case_idx: # 첫 번째 실행일 때 고려 or 2번째부터
        case_min = min(all_case[i])
        case_idx = all_case[i].index(case_min) # index 추출
        index_case.append(case_idx)
        # print(str(i)+'하나')
    elif index_case[i-1] == case_idx: # 같은 경우에는 두 번째 세번째를 탐색해야함.
        case_idx = second_min(all_case[i])
        case_min = all_case[i][case_idx]
        index_case.append(case_idx)
        # print(str(i) + '둘')
    print(case_min)
    print(case_idx)
    value += case_min

print(all_case)
print(value)
print(index_case)
