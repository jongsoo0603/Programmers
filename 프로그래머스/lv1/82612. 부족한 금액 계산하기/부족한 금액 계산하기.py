def solution(price, money, count):
    
    if sum([i*price for i in range(1, count+1)]) - money < 0:
        return 0
    else :
        return sum([i*price for i in range(1, count+1)]) - money
    
    # max(0,음수)=0 <=> max(0,양수)양수
    """return max(0, sum([i*price for i in range(1, count+1)]) - money)"""
    