def solution(array, commands):
    answer = []   
    return [sorted(array[a[0]-1 : a[1]])[a[2]-1] for a in commands]