def solution(s):
    n = len(s)
    return s[n//2] if n % 2 != 0 else s[n//2-1:n//2+1]