import os
import random


class Maze:
    maze = []
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

        if width % 2 == 0 or height % 2 == 0:
            print("\u001b[31m" + "Width and height must be odd number" + "\u001b[0m")
            raise ValueError
        else:
            self.generate()
            self.maze[0][1], self.maze[height-1][width-2] = False, False

    def generate(self):
        self.maze = [[True for _ in range(self.width)] for _ in range(self.height)]
        self.open((1, 1))

    def open(self, block):
        x, y = block
        self.maze[y][x] = False
        way = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(way)

        while way:
            next_block = way.pop()
            next_x, next_y = next_block
            if 0 < next_x < self.width and 0 < next_y < self.height and self.maze[next_y][next_x]:
                self.maze[(y + next_y) // 2][(x + next_x) // 2] = False
                self.open(next_block)

    def print(self):
        for h in range(len(self.maze)):
            for w in range(len(self.maze[0])):
                if self.maze[h][w]:
                    print("⬛", end="")
                else:
                    print("⬜", end="")
            print("")
        print("")

    def save(self, save_path):
        path = os.path.join(os.getcwd(), save_path)
        f = open(path, "w", encoding="utf_8")

        for h in range(len(self.maze)):
            for w in range(len(self.maze[0])):
                if self.maze[h][w]:
                    f.write("⬛")
                else:
                    f.write("⬜")
            f.write("\n")
        f.close()

        print(f"Saved in {path}")
