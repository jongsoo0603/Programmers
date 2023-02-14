# 테스트는 통과 하는데 왜 안되는지 모르겠음
"""
def solution(s):
    answer = ""
    for wrd in s.split(" "):
        if wrd != '':
            for i in range(len(wrd)):
                if i % 2 ==0:
                    answer += wrd[i].upper()
                else:
                    answer += wrd[i].lower()
            answer += " "
    return answer.strip()
"""
def solution(s):
    a=[]
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                a.append(s[i][j].upper())
            else:
                a.append(s[i][j].lower())
        a.append(" ")

    c="".join(a[:-1])
    return c