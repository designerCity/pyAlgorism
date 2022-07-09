word1, word2 = list(input().split())


for i in range(0, 3):
    word1[i] = word1[2-i]
    word2[i] = word2[2-i]

print(max(word1, word2))