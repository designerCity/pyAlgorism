num_list = []

for i in range(3):
    num_list.append(int(input()))


result = list(str(num_list[0] * num_list[1] * num_list[2]))
for i in range(10):
    # count 
    print(result.count(str(i)))


