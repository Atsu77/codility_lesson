def solution(A):
    result = len(A) + 1
    for N in range(len(A)):
        result ^= (N+1) ^ A[N]

    return result



A=[2 ,3 ,1 ,5]
print(solution(A))