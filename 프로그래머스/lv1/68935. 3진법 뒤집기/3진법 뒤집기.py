def solution(n):
    a = []
    while n != 0 :
        a.insert(0,n % 3)
        n = n // 3 
    return sum([a[i] * (3 ** i) for i in range(len(a))])