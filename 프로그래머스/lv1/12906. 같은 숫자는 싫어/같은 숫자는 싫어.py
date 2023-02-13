"""def solution(arr):
    answer = [arr[0]]
    answer += [arr[i] for i in range(1, len(arr)) if arr[i-1] != arr[i]]
    return answer"""
    
def solution(arr):
    answer = []
    for i in arr:
        if (len(answer) == 0) or (answer[-1] != i):
            answer.append(i)
    return answer