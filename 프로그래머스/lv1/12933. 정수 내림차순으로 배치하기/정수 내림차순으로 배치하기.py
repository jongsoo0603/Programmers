def solution(n):
    answer = 0
    array = []
    a = str(n)
    for i in range(0, len(a)):
        array.append(a[i])
    array.sort(reverse=True)
    print(array)
    return answer