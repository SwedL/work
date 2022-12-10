


def solution(s, t):
    def rec(s, t, x2=0):
        if s <= 0:
            return s
        if t <= 0:
            return 0
        if x2 == 1:
            return s + rec(s, t-1, x2=0)
        return max(s + rec(s, t-1, x2=0), s*2 + rec(s-1, t-1, x2=1))
    return rec(s, t)


print(solution(10, 11))

#print(solution(937, 56))