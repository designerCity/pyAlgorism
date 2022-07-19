arr_how = list(map(str, input().split()))
arr = list(map(int, input().split()))
length = len(arr)
price = 0
result = []
for i in range(length):
    result.append(str(arr[i]) + ' ' + arr_how[i])
    price += arr[i]
# while length >0:    
#     price += arr[-1]
#     result.append(arr_how[-1] + ' ' + str(arr[-1]))
#     length -= 1

print(result)
print(price)
