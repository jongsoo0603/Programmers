def solution(phone_number):
    s = list(phone_number)
    for i in range(0, len(s)-4):
        s[i]="*"
    return "".join(s)