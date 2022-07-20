n = int(input())
cnt = 0 # 몇 번째인지 확인하는 값
fst_num = 666 #출력해야하는 값
num_list = []
# 정수를 str 로 변환하여 666이 연속으로 들어가는 지 보기 위해 문자열 666 이 들어가는 지 확인해준다. 
while n > 0:
    if '666' in str(fst_num):    
        cnt += 1
    if cnt == n:
        break
    fst_num += 1
print(fst_num)
