import unittest
import random


def solution(A):
    def is_intersect(ma, mb, ra, rb):
        d = abs(ma - mb)
        return d <= ra + rb
    
    mr = []
    for m, r in enumerate(A):
        mr.append([m, r])
    
    cnt = 0
    import itertools
    for j, k in itertools.combinations(mr, 2):
        if is_intersect(j[0], k[0], j[1], k[1]):
            cnt += 1
    
    return cnt


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    #def test_extreme_small(self):
    #    self.assertEqual(solution([]), 0)
    #    self.assertEqual(solution([10]), 0)
    #    self.assertEqual(solution([1, 1]), 1)

    #def test_extreme_large(self):
    #    A = [10000000] * 100000
    #    self.assertEqual(solution(A), -1)


if __name__ == '__main__':
    unittest.main()