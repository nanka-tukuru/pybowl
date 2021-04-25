class PyBowl:
    """ボーリングスコア計算サンプル
    テストユニットを動かすためのサンプルで、
    フレーム単位にスコアを追加して合計するだけ
    (スペア、ストライク等の考慮なし)
    """

    def __init__(self):
        self._frame_score = []

    def add_frame_score(self, score1, score2, score3):
        """フレームのスコアを追加
        3投分のスコアをタプルにして追加
        (スペア、ストライク等の考慮なし)
        """
        self._frame_score.append((score1, score2, score3))

    def get_total_score(self):
        """全フレームのスコアの合計を取得
        単純にスコアを合計して返す
        (スペア、ストライク等の考慮なし)
        """
        total = 0
        for score in self._frame_score:
            for part in score:
                if part != None:
                    total += part
        return total
