def solution(A):
    if set(A) == set(range(1, len(A)+1)):
        return 1
    else:
        return 0

# testcase 1
A = [4 ,1 ,3, 2]
print(solution(A))

# testcase 2
A = [4 ,1 ,3]
print(solution(A))

# testcase 3
A = [2]
print(solution(A))