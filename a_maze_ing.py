# a_maze_ing.py
"""
仮の main ファイル
・迷路を生成する
・ASCIIで表示する
（config や file 出力はまだ）
"""

from maze.generator import MazeGenerator
from maze.renderer import ASCIIRenderer


def main() -> None:
    # ===== 仮パラメータ =====
    width = 10
    height = 6
    seed = None  # 再現性確認用（None にしてもOK）

    # ===== 迷路生成 =====
    maze = MazeGenerator(width=width, height=height, seed=seed)
    maze.generate()

    # ===== 表示 =====
    renderer = ASCIIRenderer()
    renderer.render(maze)


if __name__ == "__main__":
    main()
