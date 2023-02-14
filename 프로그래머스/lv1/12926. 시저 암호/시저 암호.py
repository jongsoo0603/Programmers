def solution(s, n):
    answer = ''
    uplst = list(range(65,91))
    lwlst = list(range(97,123))
    for i in s:
        if i.isupper():
            if ord(i)+n > 90:
                answer += chr(ord(i)+n - 26)
            else:
                answer += chr(ord(i)+n)
        elif i.islower():
            if ord(i)+n > 122:
                answer += chr(ord(i)+n - 26)
            else:
                answer += chr(ord(i)+n)
        else :
            answer += " "
    return answer

# 범위 계산해서 코드 줄이기
"""
def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr((ord(i) +n -ord('A')) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i) +n -ord('a')) % 26 + ord('a'))
        else :
            answer += " "
    return answer
"""
