import sys
input = sys.stdin.readline

word = input().rstrip()

# 알파벳 a ~ z 가 총 26개
arr = [[0] * 26]
arr[0][ord(word[0]) - 97] = 1

# 이게 핵심인 것 같다.
for i in range(1, len(word)):
    arr.append(arr[-1][:])  # arr 전 행을 그대로 이전
    # 여기서 시간 단축하는 것이 중요하다.
    arr[i][ord(word[i]) - 97] += 1 # 이전한 행에 해당하는 문자열을 더해줌

for _ in range(int(input())):
    a, str, end = list(input().split())
    str, end = map(int, [str, end])
    # 주석 같은 방식으로 하는 것보다 다른 변수를 이용하는 것이 시간은 단축되지만, 메모리를 더 차지하는 것 같다.
    # a, b, c = input().split()
    # start, end = map(int, [b, c])
    if str == 0:
        print(arr[end][ord(a) - 97])
    else:
        print(arr[end][ord(a) - 97] - arr[str -1][ord(a) - 97])
