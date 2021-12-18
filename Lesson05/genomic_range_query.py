import unittest
import random

# maximum number of neucleotides in a sequence
MAX_N = 100000
# maximum number of queries
MAX_M = 50000
map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

def solution(S, P, Q):
    result = []
    for p, q in zip(P, Q):
        slice = sorted(S[p:q+1])
        result.append(map[slice[0]])
    return result

class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution('CAGCCTA', [2,5,0], [4,5,6]), [2, 4, 1])

    def test_random(self):
        seq = [random.choice("ACGT") for _ in range(1, 5000)]
        P_array, Q_array = [], []
        for _ in range(0, len(seq)):
            P = random.randint(0, len(seq)-1)
            Q = random.randint(P, len(seq)-1)
            P_array.append(P)
            Q_array.append(Q)
        solution(seq, P_array, Q_array)

    def test_extreme(self):
        S = 'T' * MAX_N
        P = [0] * MAX_M
        Q = [MAX_N - 1] * MAX_M
        self.assertEqual(solution(S, P, Q), [4] * MAX_M)

if __name__ == '__main__':
    unittest.main()