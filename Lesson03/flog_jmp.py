import math

def solution(X, Y, D):
    return math.ceil((Y-X)/D)


X = 10
Y = 85
D = 30

print(solution(X, Y, D))