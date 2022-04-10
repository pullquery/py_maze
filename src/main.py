from maze import Maze
from cli import cli


width, height, is_print, save_path = cli()
print(save_path)

maze = Maze(width, height)
if is_print:
    maze.print()
if save_path != None:
    maze.save(save_path)
