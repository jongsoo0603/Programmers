def solution(arr, divisor):
    answer = []
    answer = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0]
    answer.sort()
    if answer == []:
        answer.append(-1)
    return answer