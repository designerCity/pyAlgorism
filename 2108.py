import sys
from typing import Counter
n =int(input())
n_list =[]

for _ in range(n):
    num_input = int(sys.stdin.readline())
    n_list.append(num_input)

# 평균
print(round(sum(n_list)/n))

# 중앙값
n_list.sort()
print(n_list[int((n-1)/2)])

# 최빈값
# counter 라이브러리를 사용하면 효율적으로 접근이 가능하다.
# n_counter 는 (값, 빈도수) 형태로 출력된다.
n_counter = Counter(n_list).most_common()
if len(n_counter) > 1:  
    if n_counter[0][1] == n_counter[1][1]: # 최대 빈도와 두 번째 빈도가 같을 때
        print(n_counter[1][0])
    else: # 유일한 최대 빈도를 가질 때
        print(n_counter[0][0])
else:
    print(n_counter[0][0])


# 범위 : 최댓값과 최솟값의 차이
num_range = n_list[-1] - n_list[0] 
print(num_range)
