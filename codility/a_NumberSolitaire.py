import unittest


def solution(A):
    if len(A) == 0:
        return 0
    A = [abs(A[i]) for i in range(len(A))]  # O(N)

    max_value = max(A)
    count = [0] * (max_value + 1)
    for a in A:
        count[a] += 1

    total_sum = sum(A)  # O(N)

    dp = [-1] * (total_sum + 1)
    dp[0] = 0

    for a in range(1, max_value + 1):
        if count[a] <= 0:
            continue
        for partial_sum in range(total_sum):
            if dp[partial_sum] >= 0:  # partial_sum을 만드는데 a는 사용하지 않았으므로
                dp[partial_sum] = count[a]  # dp[partial_sum]을 count[a] 로 초기화

            elif partial_sum >= a and dp[partial_sum - a] > 0:  # partial_sum - a 를 만들고 남은 a의 수가 0 보다 크면
                dp[partial_sum] = dp[partial_sum - a] - 1  # partial_sum 을 만들면 남은 a의 수 - 1 일 것이다.

    for partial_sum in range(total_sum // 2, -1, -1):
        if dp[partial_sum] >= 0:
            return total_sum - 2 * partial_sum
    return 0


class MinAbsSumTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(0, solution([1, 5, 2, -2]))

    def test_example2(self):
        self.assertEqual(50, solution([5, -1, 99, -43]))

    def test_example3(self):
        self.assertEqual(0, solution([-1, -1, -1, -1]))

    def test_example4(self):
        self.assertEqual(1, solution([-1, -1, -1]))

    def test_example5(self):
        self.assertEqual(1, solution([1, 1, 1]))

    def test_example6(self):
        self.assertEqual(0, solution([3, 3, 3, 4, 5]))