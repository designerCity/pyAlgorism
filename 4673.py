numbers = list(range(1, 10_001))
remove_list = []
for num in numbers:
    for i in str(num):
        num += int(i)
    if num <= 10000:
        remove_list.append(num)

for remove_num in set(remove_list):
    numbers.remove(remove_num)

for self_num in numbers:
    print(self_num)

### list set 의 차집합을 사용한 코드 -- 답안지 봄.

# numbers = set(range(1, 10000))
# remove_set = set()  # 생성자가 있는 숫자 set
# for num in numbers :
#     for n in str(num):
#         num += int(n)
#     remove_set.add(num)  # add: 집합에 요소를 추가할 때

# self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
# for self_num in sorted(self_numbers):  # sorted 함수로 정렬
#     print(self_num)