import sys
tile = int(sys.stdin.readline())  # 타일의 길이
dp = [0] * 100001
dp[1] = 1
dp[2] = 2

for i in range(3, tile+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[tile])
