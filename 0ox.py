# 백준 8958번 
N=input()
for i in range(N):
    rlt=input()
    result=list(rlt)
    sum=0
    f=1
    for k in result:
        if k =='O':
            sum+=f
            f+=1
        else:
            f=1
    print(sum)