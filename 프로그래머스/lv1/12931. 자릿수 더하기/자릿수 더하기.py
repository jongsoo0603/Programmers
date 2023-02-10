def solution(n):
    answer = 0
    
    a = n
    length = len(str(n))
    for i in range(1, length+1):
        b = a % 10
        a = a // 10
        answer += b
    return answer