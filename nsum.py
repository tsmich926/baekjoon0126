#정수n개의 합을 구하는 함수 백준 15596
def nsum(a):
    sum=0
    for i in a:
        sum+=i
    return sum

nsum(2,3)