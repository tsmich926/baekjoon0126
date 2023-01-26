#백준 10818
N=input()
s=list(map(int,input().split()))
min=2344252
max=0
for i in s:
    if i > max :
        max=i
    if i < min :
        min=i
print(min,max)

