len_a, len_b = map(int, input().split())
a = set(input().split())
b = set(input().split())
print(len((a-b) | (b-a)))