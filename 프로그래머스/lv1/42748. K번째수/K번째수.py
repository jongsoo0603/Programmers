def solution(array, commands):
    answer = []
    #answer.append( sorted(array[commands[0][0]-1 : commands[0][1]])[3-1] )
    for a in commands:
        answer.append( sorted(array[a[0]-1 : a[1]])[a[2]-1] )
    return answer