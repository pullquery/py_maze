import random

class Maze:
    maze = []
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

        if width % 2 == 0 or height % 2 == 0:
            raise ValueError
        else:
            self.generate()


    def generate(self):
        self.maze = [[True for _ in range(self.width)] for _ in range(self.height)]
        self.open_block((1, 1))


    def open_block(self, block):
        x, y = block
        self.maze[y][x] = False

        print(block)
        self.print()
        
        next_block = self.choice_block(block)
        self.open_block(next_block)

            
    def choice_block(self, block):
        x, y = block

        next_block = random.choice(((x+2, y), (x-2, y), (x, y+2), (x, y-2)))
        next_x, next_y = next_block
        if 0 < next_x < self.width and 0 < next_y < self.height and self.maze[next_y][next_x]:
            return next_block
        else:
            return self.choice_block(block)


    def print(self):
        for h in range(len(self.maze)):
            for w in range(len(self.maze[0])):
                if self.maze[h][w]:
                    print("⬛", end="")
                else:
                    print("⬜", end="")
            print("")
        print("")


maze = Maze(11, 11)
maze.print()
