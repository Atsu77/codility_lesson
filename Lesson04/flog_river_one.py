def solution(X, A):
    n = [-1] * (X + 1)
    for idx, i in enumerate(A):
        if n[i] == -1:
            n[i] = idx
        else:
            continue
    
    if -1 not in n[1:]:
        return max(set(n))
    
    return -1


# testcase 1
X = 5
A = [1 ,3 ,1 ,4 ,2 ,3, 5, 4]
print(solution(X , A))

# testcase 2
X = 2
A = [2 ,2 ,2 ,2]
print(solution(X , A))

# testcase 3
X = 3
A = [1, 3, 1, 3, 2, 1, 3]
print(solution(X , A))

# testcase 4
X = 1
A = [1]
print(solution(X , A))