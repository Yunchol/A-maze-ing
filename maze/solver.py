#BFS

from collections import deque
from typing import Dict, List, Optional, Tuple

from maze.generator import MazeGenerator


class MazeSolver:
    """
    迷路の ENTRY から EXIT までの最短経路を探すクラス
    """

    def solve(
        self,
        maze: MazeGenerator,
        entry: Tuple[int, int],
        exit: Tuple[int, int],
    ) -> List[str]:
        """
        ENTRY から EXIT までの最短経路を N/E/S/W のリストで返す
        """
        start_x, start_y = entry
        goal_x, goal_y = exit

        queue = deque()
        queue.append((start_x, start_y))

        visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]
        visited[start_y][start_x] = True

        # 「どこから来たか」を覚える
        prev: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]] = {}

        directions = {
            "N": (0, -1),
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0),
        }

        while queue:
            x, y = queue.popleft()

            # ゴールに着いたら終了
            if (x, y) == (goal_x, goal_y):
                return self._reconstruct_path(prev, entry, exit)

            cell = maze.get_cell(x, y)

            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy

                # 迷路の外
                if not (0 <= nx < maze.width and 0 <= ny < maze.height):
                    continue

                # 壁があるなら行けない
                if cell.has_wall(direction):
                    continue

                # もう行った場所
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                prev[(nx, ny)] = ((x, y), direction)
                queue.append((nx, ny))

        # 通れない場合（PERFECT なら基本起きない）
        return []

    def _reconstruct_path(
        self,
        prev: Dict[Tuple[int, int], Tuple[Tuple[int, int], str]],
        entry: Tuple[int, int],
        exit: Tuple[int, int],
    ) -> List[str]:
        """
        prev を使って経路を逆にたどる
        """
        path: List[str] = []
        current = exit

        while current != entry:
            previous, direction = prev[current]
            path.append(direction)
            current = previous

        path.reverse()
        return path
