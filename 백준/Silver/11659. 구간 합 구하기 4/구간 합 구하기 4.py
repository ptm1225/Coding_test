n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] += arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i-2 < 0:
        print(arr[j-1])
    else:
        print(arr[j-1]-arr[i-2])