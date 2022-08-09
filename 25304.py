# 영수증
price_sum = int(input())
menu_num = int(input())

srch_sum = 0
for _ in range(menu_num):
    a, b = map(int, input().split())
    srch_sum += a * b
if srch_sum == price_sum:
    print('Yes')
else:
    print('No')