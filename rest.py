#백준3052 서로다른 나머지가 몇개 있는지 출력

lst=[]
for i in range(10):
    nums=int(input())
    k=nums%42
    lst.append(k)

lst=set(lst)
print(len(lst))
# set함수로 list중복 제거한뒤
# list len으로 길이 구해서 서로 다른거 갯수구함
