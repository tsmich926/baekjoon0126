#5597jun
#숙제안한사람 두명 골라내기
# num=list(map(input().split()))
# print(num)
lst=[]
for i in range(1,31):
    lst.append(i)

for k in range(28):
    subm=int(input())
    lst.remove(subm)

for m in lst:
    print(m)