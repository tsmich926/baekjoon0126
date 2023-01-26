#2562번 백준
# lst=[]
# for i in range(9):
#     n=int(input())
#     lst.append(n)
# print(lst)
# idx=lst.find(max(lst))
# print(idx)

lst=[]
for i in range(9):
    n=int(input())
    lst.append(n)
# print(lst)
print(max(lst))
print(lst.index(max(lst))+1)