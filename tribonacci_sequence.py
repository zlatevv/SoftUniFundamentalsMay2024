def tribonacci_sequence(n):
    if n <= 0:
        return
    
    
    tribonacci = [1, 1, 2]
    if n <= 3:
        print(" ".join(map(str, tribonacci[:n])))
        return
    for _ in range(3, n):
        next_value = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        tribonacci.append(next_value)

    print(" ".join(map(str, tribonacci)))

n = int(input())
tribonacci_sequence(n)
