import unittest

from leetCode.solution_binary import Solution


class MyTestCase(unittest.TestCase):
    def test_that_addition_is_returned_in_binary(self):
        solution = Solution()
        answer = solution.addBinary("11", "1")
        self.assertEqual("100", answer)

    def test_that_addition_two_is_returned_in_binary(self):
        solution = Solution()
        answer = solution.addBinary("1010", "1011")
        self.assertEqual("10101", answer)



if __name__ == '__main__':
    unittest.main()
