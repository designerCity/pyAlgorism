num_list = []

for i in range(10):
    num_list.append(int(input()))

left_num = []
for j in num_list:
    left_num.append(j % 42)

left_num = set(left_num)
print(len(left_num))