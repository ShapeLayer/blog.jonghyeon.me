E = -1
X = -2

class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f'Pos (x: {self.x}, y: {self.y})'

class Solve:
    def __init__(self, map: list):
        self.map = map
        self.width = len(map[0])
        self.height = len(map)
        self.visited = [[0 for _i in range(self.width)] for _j in range(self.height)]
        self.adj = [[False for _i in range(self.width * self.height)] for _j in range(self.width * self.height)]
        self.delta = (Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1))
        self.queue = []
        self.__result = []
        self.__init_adj()
    @property
    def result(self) -> str:
        self.__result = []
        for row in self.visited:
            self.__result.append(' '.join(map(str, row)))
        return '\n'.join(self.__result)
    def __init_adj(self):
        for i in range(self.width):
            for j in range(self.height):
                now = Pos(i, j)
                for dt in self.delta:
                    new: Pos = now + dt
                    if self.pos_is_over(new): continue
                    if self.is_blocked(new): continue
                    self.adj[now.x + now.y * self.width][new.x + new.y * self.width] = True
                    self.adj[new.x + new.y * self.width][now.x + now.y * self.width] = True
    def pos_is_over(self, pos: Pos) -> bool:
        return pos.x < 0 or pos.x >= self.width or pos.y < 0 or pos.y >= self.height
    def is_blocked(self, pos: Pos) -> bool:
        return self.map[pos.y][pos.x] == 1
    def proc(self):
        while self.queue:
            now = self.queue.pop(0)
            pos, step = now
            step += 1
            if self.map[pos.y][pos.x] == X: 
                break
            for dt in self.delta:
                new: Pos = pos + dt
                if self.pos_is_over(new): continue
                if self.is_blocked(new): continue
                if self.visited[new.y][new.x] == 0:
                    self.visited[new.y][new.x] = step
                    self.queue.append((new, step))

if __name__ == '__main__':
    gets = [
        [1, 1, 1, 1, 1, 1],
        [E, 0, 0, 0, 0, 1], # -1 = e
        [1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, X], # -2 = x
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    solve: Solve = Solve(gets)
    start = Pos(0, 1)
    solve.visited[start.y][start.x] = 1
    solve.queue.append((start, 1))
    solve.proc()
    print(solve.result)
    print(f'(1, 4) to (2, 4): {solve.adj[1 + 4 * 6][2 + 4 * 6]}')
