
#? 백준1546 평균

N=int(input())
scores=list(map(int,input().split()))
# print(scores)
max_score=max(scores)
# print(max_score)

lst=[]
for i in scores:
    new_score = i/max_score*100
    lst.append(new_score)
# print(lst)
# print(len(lst))

sum=0
for s in lst:
    sum+=s
    new_av=sum/len(lst)
print(new_av)