import cProfile
from random import choice

def generate_random_integer(ln: int) -> str:
    buf: list[str] = []
    num_str = list('1234567890')
    for i in range(ln):
        buf.append(choice(num_str))
    return ''.join(buf)

def compute(n: str, x: str) -> int:
    def calc_int(n: str, x: str) -> int:
        def conversion(n: str) -> int:
            return int(n)
        return conversion(n) % conversion(x)
    def calc_str(n: str, x: str) -> int:
        remainder: int = 0
        div = int(x)
        for each in n:
            remainder = (remainder * 10 + int(each)) % div
        return remainder
    calc_int(n, x)
    calc_str(n, x)

if __name__ == '__main__':
    n = generate_random_integer(1000000) 
    x = generate_random_integer(7)
    compute(n, x)
    cProfile.run('compute(n, x)')
