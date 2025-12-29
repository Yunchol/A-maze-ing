# maze/generator.py
import random
from typing import List, Tuple

from maze.cell import Cell


class MazeGenerator:
    """
    迷路全体を管理するクラス
    """

    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")

        self.width = width
        self.height = height

        if seed is not None:
            random.seed(seed)

        self.grid: List[List[Cell]] = self._create_grid()
        self.visited: List[List[bool]] = [
            [False for _ in range(width)] for _ in range(height)
        ]

    def _create_grid(self) -> List[List[Cell]]:
        grid: List[List[Cell]] = []

        for y in range(self.height):
            row: List[Cell] = []
            for x in range(self.width):
                row.append(Cell())
            grid.append(row)

        return grid

    def get_cell(self, x: int, y: int) -> Cell:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("cell position out of range")
        return self.grid[y][x]

    # ===== ここからがステップ③ =====

    def generate(self) -> None:
        """
        迷路を生成する（道を掘る）
        """
        self._carve_from(0, 0)

    def _carve_from(self, x: int, y: int) -> None:
        """
        (x, y) からランダムに道を掘る
        """
        self.visited[y][x] = True

        directions: List[Tuple[str, int, int]] = [
            ("N", 0, -1),
            ("E", 1, 0),
            ("S", 0, 1),
            ("W", -1, 0),
        ]

        random.shuffle(directions)

        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not self._is_inside(nx, ny):
                continue

            if self.visited[ny][nx]:
                continue

            # 壁を壊す
            self._remove_walls_between(x, y, nx, ny, direction)

            # 次のマスへ
            self._carve_from(nx, ny)

    def _is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def _remove_walls_between(
        self,
        x: int,
        y: int,
        nx: int,
        ny: int,
        direction: str,
    ) -> None:
        """
        2つのマスの間の壁を壊す
        """
        opposite = {"N": "S", "S": "N", "E": "W", "W": "E"}

        current = self.get_cell(x, y)
        next_cell = self.get_cell(nx, ny)

        current.remove_wall(direction)
        next_cell.remove_wall(opposite[direction])
