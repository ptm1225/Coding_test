n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

print(arr[k-1])