num_list = []

# num_list 안에 input을 3번으로 제한해서, 3번이 채워지면 돌아가게
for i in range(3):
    num_list.append(int(input()))
# 0부터 9까지 수가 몇 번 들어가는지 알아보게 하는 함수
result = list(str(num_list[0] * num_list[1] * num_list[2]))
for i in range(10):
    # count 
    print(result.count(str(i)))


