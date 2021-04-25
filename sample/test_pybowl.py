import unittest
from pybowl import PyBowl

class TestPyBowl(unittest.TestCase):
    """PyBowlテスト
    標準ライブラリのunittestの簡単なサンプル
    なお、カバレッジは計測できない
    (他のモジュールを使えば可能)
    """

    def test_case1(self):
        """add_frame_score test
        """
        test_case = [
            (None, None, None),
            (1, None, None),
            (1, 2, None),
            (1, 2, 3),
        ]
        pybowl = PyBowl()
        for case in test_case:
            pybowl.add_frame_score(case[0], case[1], case[2])
        for case_idx in range(len(test_case)):
            self.assertTupleEqual(pybowl._frame_score[case_idx],
                                  test_case[case_idx])

    def test_case2(self):
        """get_total_score test
        """
        test_case = [
            (10, None, None),
            (5, 5, None),
            (0, 10, None),
            (10, None, None),
            (10, None, None),
            (10, None, None),
            (10, None, None),
            (10, None, None),
            (10, None, None),
            (10, 10, 10),
        ]
        pybowl = PyBowl()
        for case in test_case:
            pybowl.add_frame_score(case[0], case[1], case[2])
        total = pybowl.get_total_score()
        self.assertEqual(total, 120)

if __name__ == "__main__":
    unittest.main()
