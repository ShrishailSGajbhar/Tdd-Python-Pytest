def fibonacci(N):
    if (N <= 0):
        return []
    if (N == 1):
        return [0]
    result = [0, 1]
    if (N == 2):
        return result
    for i in range(2, N):
        result.append(result[i-2] + result[i-1])
    return result
