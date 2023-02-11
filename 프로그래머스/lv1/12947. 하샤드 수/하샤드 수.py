def solution(x):
    b = 0
    a = [int(i) for i in str(x)]
    
    for j in a:
        b += j
    
    if x % b == 0:
        return True
    else :
        return False