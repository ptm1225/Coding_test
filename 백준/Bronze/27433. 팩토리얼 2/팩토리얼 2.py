def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

print(fac(int(input())))