def solution(left, right):

    # 0. 원래 스타일
    """
    answer = 0
    a = []
    for i in range(left, right+1):
        for j in range(1, (i//2)+1):
            if i % j == 0:
                a.append(j)
        if (len(a)+1) % 2 ==0:
            answer += i
        else :
            answer -= i
        a = []
    return answer
    """
    
    # 1. 2차 for문에 2차 if문 합치기
    """
    answer = 0
    for i in range(left, right+1):
        a = [j for j in range(1, (i//2)+1) if i % j == 0]
        if (len(a)+1) % 2 ==0:
            answer += i
        else :
            answer -= i
        a = []
    return answer
    """
    
    # 2. 2차 for문에 1차 if문 합치기 
    """
    answer = 0
    for i in range(left, right+1):
        if (len([j for j in range(1, (i//2)+1) if i % j == 0])+1) % 2 == 0:
            answer += i
        else :
            answer -= i
    return answer
    """
    # 3. 1차 for문에 다 합치기
    return sum([i if (len([j for j in range(1, (i//2)+1) if i % j == 0])+1) % 2 == 0 else -i for i in range(left, right+1)])
