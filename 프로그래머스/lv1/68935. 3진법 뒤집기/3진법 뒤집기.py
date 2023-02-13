def solution(n):
    a = []
    while n != 0: # == while n :
        a.insert(0,n % 3)
        n = n // 3 
    return sum([a[i] * (3 ** i) for i in range(len(a))])


# int(tmp,3) 3진법 temp 문자열을 10진수로
"""
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
"""