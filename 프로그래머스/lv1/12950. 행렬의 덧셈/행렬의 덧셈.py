def solution(arr1, arr2):
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

# 빈 리스트에는 값을 넣을 수 없어서 .append()나 .insert()를 사용해야 한다.
# 하지만 중첩리스트는 [[4],[6],[7],[9]] 이렇게 되기 때문에 힘들었음
    """
    def solution(arr1, arr2):
        answer = [[]]
        for i in range(len(arr1)):
            for j in range(len(arr1[i])):
                answer[i][j] = arr1[i][j] + arr2[i][j]
        return answer
    """