N,b = map(int, input().split())
A = list(map(int, input().split()))


    # N 는 랜덤한 몇 개의 수를 주는 변수
    # b 는 기준값
    
for i in range(N):
    if A[i] < b:
        print(A[i],end=' ')
# end 옵션을 사용하면 각 print 문을 이어서 출력하여 줄바꿈을 하지 않을 수 있다.
