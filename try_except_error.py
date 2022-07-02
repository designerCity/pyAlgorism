# 입력이 여러 값일 때
while 1:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
# try except 문은 error 가 일어났을 때 판가름하는 구문
# JS 와는 다르게 try except문을 사용한다. 
# 테스트 케이스 개수가 정해지지 않았기 때문에
# try: 변수 A,B에 int형이 들어간다면, A+B의 값을 출력한다.
# except: try에 대한 에러가 발생
