t = int(input()) # t test 개수
num_li = list(map(int, input().split()))
operator_li = list(map(int, input().split()))

opr = ['+', '-', '*', '//']
op = [] # 가질 수 있는 연산자의 수 

# 연산자 배치부터 신경 써야한다.
for k in range(len(operator_li)):
    for i in range(operator_li[k]):
        op.append(opr[k])



# 배치해야하는 것의 개수 t -1 
print(op)
print(opr)