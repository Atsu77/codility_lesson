import unittest
import random


RANGE_A = (-1000, 1000)
RANGE_N = (3, 100000)


def solution(A):
    A.sort()
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
    else:
        return A[-3] * A[-2] * A[-1]


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([-3, 1, 2, -2, 5, 6]), 60)

    def test_sample(self):
        self.assertEqual(solution([-5, 5, -5, 4]), 125)

    def test_zero(self):
        self.assertEqual(solution([0, 0, 0, 0]), 0)
        self.assertEqual(solution([-10, -10, -3, 0, 1]), 100)

    def test_negative(self):
        self.assertEqual(solution([-4, -3, -2, -1]), -6)
        self.assertEqual(solution([-1, -1, 1, 2]), 2)
        self.assertEqual(solution([-5, -5, 1, 2]), 50)
        self.assertEqual(solution([-5, -5, -1, 0]), 0)

    def test_large(self):
        self.assertEqual(solution([1000, 1000, 1000]), int(1e9))

    def test_extreme(self):
        A = [random.randint(*RANGE_A) for _ in range(3, 99997)]
        A += [1000, 1000, 1000]
        self.assertEqual(solution(A), int(1e9))


if __name__ == '__main__':
    unittest.main()
