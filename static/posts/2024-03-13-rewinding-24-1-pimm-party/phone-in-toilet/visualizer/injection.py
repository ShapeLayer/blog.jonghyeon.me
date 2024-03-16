'''
How to use:
1. import this file and initialize CaseBuffer.
2. call CaseBuffer.input_screws() after get input about screws.
3. call CaseBuffer.input_weaks() after get input about weak components.
4. call CaseBuffer.input_hull() after check each convex hull.
5. call CaseBuffer.set_injection_level() call if manage value about water injection level.
'''

from json import dumps

class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Dot (x: {self.x}, y: {self.y})'
    
    def to_dict(self):
        return self.__dict__

class CaseBuffer:
    def __init__(self):
        self.screws: list[Dot] = []
        self.weaks: list[Dot] = []
        self.conns: list[list[Dot]] = []
        self.level: int = -1

    def input_screws(self, screws: list[list[int]]):
        for each in screws:
            x, y = each[0], each[1]
            self.screws.append(Dot(x, y))
        print('CaseBuffer: Updated screws.')

    def input_weaks(self, weaks: list[list[int]]):
        for each in weaks:
            x, y = each[0], each[1]
            self.weaks.append(Dot(x, y))
        print('CaseBuffer: Updated weaks.')
    
    def input_hull(self, hull: list[list[int]]):
        conn: list[Dot] = []
        for each in hull:
            x, y = each[0], each[1]
            conn.append(Dot(x, y))
        self.conns.append(conn)
        print('CaseBuffer: Added new convex hull.')
    
    def set_injection_level(self, level: int):
        self.level = level
        print('CaseBuffer: Updated injection level.')
    
    def save(self, filename: str='input.json'):
        output = {
            'screws': [*map(lambda each: each.to_dict(), self.screws)],
            'weaks': [*map(lambda each: each.to_dict(), self.weaks)],
            'conns': [
                [*map(lambda each: each.to_dict(), conn)] for conn in self.conns
            ],
            'level': self.level
        }
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(dumps(output, indent=4))
        print('CaseBuffer: Save done.')
