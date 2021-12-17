def solution(N, A):
    cnt = [0] * (N + 1)
    for i in A:
        if(i == N + 1):
            cnt = [max(cnt)] * (N + 1)
        else:
            cnt[i] += 1
    return cnt[1:]

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))