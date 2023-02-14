def solution(d, budget):
    cnt = 0
    for i in range (len(d)):
        print(sorted(d)[i])
        budget -= sorted(d)[cnt]
        if budget < 0:
            break
        cnt += 1
    return cnt