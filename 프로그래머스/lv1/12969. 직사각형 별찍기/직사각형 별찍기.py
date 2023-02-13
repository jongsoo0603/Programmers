a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

# 한 줄 풀이
"""
print(('*'*a +'\n')*b)
"""