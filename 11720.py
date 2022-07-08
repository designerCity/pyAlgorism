a = int(input())

numbers = input()
total = 0
for i in str(numbers):
    total += int(i)

print(total)

# # sum 함수를 이용하는 방법
# n = input()

# print(sum(map(int,input())))


# # 문자열의 특성을 이용하는 방법
# n = input()
# nums = input()
# total = 0
# for i in range(n) :  # 0부터 n-1까지
#     total += int(nums[i])
# print(total)