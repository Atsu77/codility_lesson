import unittest
import random


RANGE_A = (2, 100000)
RANGE_N = (-10000, 10000)


def solution(A):
    min_avg = RANGE_N[1]
    lowest_idx = 0
    last = None
    second_last = None
    for idx, this in enumerate(A):
        if second_last is not None:
            three_avg = (second_last + last + this) / 3
            if three_avg < min_avg:
                min_avg = three_avg 
                lowest_idx = idx - 2
        if last is not None:
            second_avg = (last + this) / 2
            if second_avg < min_avg:
                min_avg = second_avg
                lowest_idx = idx - 1
        
        second_last = last
        last = this
    return lowest_idx


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]), 1)
        self.assertEqual(solution([5, 2, 2, 100, 1, 1, 100]), 4)
        self.assertEqual(solution([11, 2, 10, 1, 100, 2, 9, 2, 100]), 1)

    def test_three(self):
        # self.assertEqual(solution([-3, -5, -8, -4, -10]), 2)
        # self.assertEqual(solution([-8, -6, -10]), 0)
        self.assertEqual(solution([1, -1, 1, -1]), 1)

    def test_random(self):
        A = [random.randint(*RANGE_N) for _ in xrange(2, 10)]
        print A
        print solution(A)

    def test_large_ones(self):
        """Numbers from -1 to 1, N = ~100000"""
        # how to test?

    def test_extreme(self):
        A = [RANGE_N[1]] * (RANGE_A[1] / 3) + [RANGE_N[0]] * (RANGE_A[1] / 3)
        idx = solution(A)
        print idx, A[idx-3:idx+3]

if __name__ == '__main__':
    unittest.main()
