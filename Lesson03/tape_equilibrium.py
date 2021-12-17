def solution(A):
    head = sum(A[0])
    tail = sum(A[1:])
    diff = abs(head - tail)
    for num in A[1:-1]:
        head += num
        tail -= num
        diff = min(diff, abs(head-tail))
    return diff


#testcase 1
A = [3, 1, 2, 4, 3]
print(solution(A))

#testcase 2
A = [-1000, 1000]
print(solution(A))