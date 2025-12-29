# maze/renderer.py
from maze.generator import MazeGenerator


class ASCIIRenderer:
    """
    迷路をターミナルに ASCII で表示するクラス
    """

    def render(self, maze: MazeGenerator) -> None:
        width = maze.width
        height = maze.height

        # 一番上の壁
        top_line = "+"
        for x in range(width):
            cell = maze.get_cell(x, 0)
            top_line += "---+" if cell.has_wall("N") else "   +"
        print(top_line)

        # 各行を描く
        for y in range(height):
            middle_line = "|"
            bottom_line = "+"

            for x in range(width):
                cell = maze.get_cell(x, y)

                # 中身（とりあえず空白）
                middle_line += "   "
                middle_line += "|" if cell.has_wall("E") else " "

                # 下の壁
                bottom_line += "---+" if cell.has_wall("S") else "   +"

            print(middle_line)
            print(bottom_line)
