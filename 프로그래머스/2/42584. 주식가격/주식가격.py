def solution(prices):
    
    times = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        for idx, s in stack:
            times[idx] += 1
        while stack and stack[-1][1] > prices[i]:
            stack.pop()
        stack.append((i, prices[i]))
    return times