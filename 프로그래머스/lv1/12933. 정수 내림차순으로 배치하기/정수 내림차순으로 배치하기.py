def solution(n):
    answer = []
    answer = [i for i in str(n)]
    answer.sort(reverse = True)
    answer = int("".join(answer))
    return answer