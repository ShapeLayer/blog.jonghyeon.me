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
        self.delta = (Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1))
        self.queue = []
        self.__result = []
        self.node_mapping = [[-1 for _i in range(self.height)] for _j in range(self.width)]
        self.node_count = 1
        self.__define_node_count()
        self.adj = [[False for _i in range(self.node_count + 1)] for _j in range(self.node_count + 1)]
        self.visited = [0 for _i in range(self.node_count + 1)]
        self.dest_node = -1
        self.__init_adj()
    @property
    def result(self) -> str:
        self.__result = []
        for i in range(self.node_count + 1):
            self.__result.append(f'{i}: {self.visited[i]}')
        return '\n'.join(self.__result)
    def __define_node_count(self):
        '''
        전체 노드의 개수를 구합니다.
        '''
        for i in range(self.width):
            for j in range(self.height):
                now = Pos(i, j)
                if self.pos_is_over(now): continue
                if self.is_blocked(now): continue
                self.node_mapping[now.x][now.y] = self.node_count
                if self.map[now.y][now.x] == X: self.dest_node = self.node_count
                self.node_count += 1
    def __init_adj(self):
        '''
        인접행렬을 초기화합니다.
        '''
        for i in range(self.width):
            for j in range(self.height):
                now = Pos(i, j)
                node_now = self.node_mapping[now.x][now.y]
                if node_now != -1:
                    for dt in self.delta:
                        new: Pos = now + dt
                        if self.pos_is_over(new): continue
                        if self.is_blocked(new): continue
                        node_new = self.node_mapping[new.x][new.y]
                        self.adj[node_now][node_new] = True
                        self.adj[node_new][node_now] = True
    def pos_is_over(self, pos: Pos) -> bool:
        return pos.x < 0 or pos.x >= self.width or pos.y < 0 or pos.y >= self.height
    def is_blocked(self, pos: Pos) -> bool:
        return self.map[pos.y][pos.x] == 1
    def proc(self):
        while self.queue:
            now = self.queue.pop(0)
            node_now, step = now
            step += 1
            if node_now == self.dest_node: break
            for node_next in range(1, self.node_count + 1):
                if not self.adj[node_now][node_next]: continue
                if self.visited[node_next] == 0:
                    self.visited[node_next] = step
                    self.queue.append((node_next, step))

if __name__ == '__main__':
    gets = [
        [1, 1, 1, 1, 1, 1],
        [E, 0, 0, 0, 0, 1], # -1 = e
        [1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, X], # -2 = x
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    solve: Solve = Solve(gets)
    solve.visited[1] = 1
    solve.queue.append((1, 1))
    solve.proc()
    print(solve.result)
    node_a = solve.node_mapping[4][2]
    node_b = solve.node_mapping[4][3]
    print(node_a, node_b)
    print(solve.adj[node_a][node_b])
