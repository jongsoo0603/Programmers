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
    answer = []
    word=s.split(" ")
    for i in word:
        part=[]
        for j in range(0,len(i)):
            if j%2==0:
                part.append(i[j].upper())
            else:
                part.append(i[j].lower())
        part="".join(part)
        answer.append(part)
    answer=" ".join(answer)
    return answer
