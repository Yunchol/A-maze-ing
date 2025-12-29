from typing import Dict


class Cell:
    """
    迷路の1マスを表すクラス
    各方向（北・東・南・西）に壁があるかどうかを持つ
    """

    def __init__(self) -> None:
        # 最初は全部壁あり
        self.walls: Dict[str, bool] = {
            "N": True,
            "E": True,
            "S": True,
            "W": True,
        }

    def has_wall(self, direction: str) -> bool:
        """
        指定方向に壁があるか返す
        """
        return self.walls[direction]

    def remove_wall(self, direction: str) -> None:
        """
        指定方向の壁を取り除く
        """
        self.walls[direction] = False

    def add_wall(self, direction: str) -> None:
        """
        指定方向の壁を追加する
        """
        self.walls[direction] = True

    def get_walls(self) -> Dict[str, bool]:
        """
        壁の状態をまとめて返す
        """
        return self.walls.copy()
