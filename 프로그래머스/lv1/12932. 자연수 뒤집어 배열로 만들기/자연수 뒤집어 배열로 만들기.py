def solution(n):
    answer = []
    
    a = n
    length = len(str(n))
    for i in range(1, length+1):
        b = a % 10
        a = a // 10
        answer.append(b)
    
    return answer

def solution(n):
    answer = []
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer
