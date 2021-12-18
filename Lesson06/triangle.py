def solution(A):
    def is_triangle(P, Q, R):
        return (P + Q > R) and (Q + R > P) and (R + P > Q)
    A.sort()
    for i in range(len(A) - 2):
        if is_triangle(A[i], A[i+1], A[i+2]):
            return 1
    return 0
