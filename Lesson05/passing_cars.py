import unittest
import random

MAX_PAIRS = int(1e9)

def solution(A):
    east = 0
    pairs = 0
    for car in A:
        if not bool(car):
            east += 1
        else:
            pairs += east
        if pairs > MAX_PAIRS:
            return -1
    return pairs


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([0, 1, 0, 1, 1]), 5)

    def test_minimal(self):
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([1]), 0)
        self.assertEqual(solution([0, 0]), 0)
        self.assertEqual(solution([1, 1]), 0)
        self.assertEqual(solution([0, 1]), 1)
        self.assertEqual(solution([1, 0]), 0)

    def test_three(self):
        self.assertEqual(solution([0, 0, 0]), 0)
        self.assertEqual(solution([0, 0, 1]), 2)
        self.assertEqual(solution([0, 1, 0]), 1)
        self.assertEqual(solution([0, 1, 1]), 2)
        self.assertEqual(solution([1, 0, 0]), 0)
        self.assertEqual(solution([1, 0, 1]), 1)
        self.assertEqual(solution([1, 1, 0]), 0)
        self.assertEqual(solution([1, 1, 1]), 0)

    def test_four(self):
        self.assertEqual(solution([0, 0, 0, 0]), 0)
        self.assertEqual(solution([0, 0, 0, 1]), 3)
        self.assertEqual(solution([0, 0, 1, 1]), 4)
        self.assertEqual(solution([0, 1, 0, 0]), 1)
        self.assertEqual(solution([0, 1, 0, 1]), 3)
        self.assertEqual(solution([0, 1, 1, 1]), 3)
        self.assertEqual(solution([1, 0, 0, 0]), 0)
        self.assertEqual(solution([1, 0, 0, 1]), 2)
        self.assertEqual(solution([1, 0, 1, 0]), 1)
        self.assertEqual(solution([1, 0, 1, 1]), 2)
        self.assertEqual(solution([1, 1, 0, 0]), 0)
        self.assertEqual(solution([1, 1, 0, 1]), 1)
        self.assertEqual(solution([1, 1, 1, 0]), 0)
        self.assertEqual(solution([1, 1, 1, 1]), 0)

    def test_extreme(self):
        self.assertEqual(solution([random.randint(0,1) for _ in range(int(1e6))]), -1)


if __name__ == '__main__':
    unittest.main()