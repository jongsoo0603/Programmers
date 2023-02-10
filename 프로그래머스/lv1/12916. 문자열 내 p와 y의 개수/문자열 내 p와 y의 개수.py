def solution(s):
    answer = True
    
    a = s.count('p') + s.count('P')
    b = s.count('y') + s.count('Y')
    if a == b:
        return True
    else :
        return False

    