# a_maze_ing.py
import sys

from config import load_config
from maze.generator import MazeGenerator
from maze.renderer import ASCIIRenderer
from maze.solver import MazeSolver


def parse_pair(value: str) -> tuple[int, int]:
    x_str, y_str = value.split(",")
    return int(x_str), int(y_str)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config_path = sys.argv[1]

    try:
        config = load_config(config_path)

        width = int(config["WIDTH"])
        height = int(config["HEIGHT"])
        entry = parse_pair(config["ENTRY"])
        exit = parse_pair(config["EXIT"])
        seed = int(config["SEED"]) if "SEED" in config else None

    except Exception as e:
        print(f"Config error: {e}")
        return

    # 迷路生成
    maze = MazeGenerator(width, height, seed)
    maze.generate()

    # 表示
    renderer = ASCIIRenderer()
    renderer.render(maze)

    # 経路探索
    solver = MazeSolver()
    path = solver.solve(maze, entry, exit)
    print("PATH:", "".join(path))


if __name__ == "__main__":
    main()
