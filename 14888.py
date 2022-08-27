import sys
input = sys.stdin.readline
t = int(input()) # t test 개수
num_li = list(map(int, input().split()))
operator_li = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == t:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return 
    if plus:
        dfs(depth + 1, total + num_li[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_li[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_li[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_li[depth]), plus, minus, multiply, divide - 1)

dfs(1, num_li[0], operator_li[0], operator_li[1], operator_li[2], operator_li[3])
print(maximum)
print(minimum)