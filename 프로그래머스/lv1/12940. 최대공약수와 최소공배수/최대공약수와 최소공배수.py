def solution(n, m):
    answer = []
    # 최소공배수 = n * m / 최대공약수
    answer.append(max([i for i in range(1, (max(n,m)//2)+1) if n % i == 0 and m % i == 0]))
    answer.append((n * m) / max([i for i in range(1, (max(n,m)//2)+1) if n % i == 0 and m % i == 0]))
    return answer

    """
    import math
    return [math.gcd(n,m),math.lcm(n,m)]
    """