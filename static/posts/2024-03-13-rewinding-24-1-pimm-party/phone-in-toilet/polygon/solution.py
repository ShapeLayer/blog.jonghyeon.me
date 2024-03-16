from sys import stdin, setrecursionlimit
setrecursionlimit(10_100)
input = stdin.readline
 
def ccw(a: list, b: list, c: list) -> int:
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1] ) - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])
 
def pos2vec(a: list, b: list) -> list:
    return [b[0] - a[0], b[1] - a[1]]
 
def is_outside(dot: list, hull: list) -> bool:
    if len(hull) == 2:
        return ccw(hull[0], hull[1], dot) or not (min(hull[0], hull[1]) <= dot <= max(hull[0], hull[1]))
 
    start = 0; end = len(hull) - 1
    while start < end:
        mid = (start + end) >> 1
        if ccw(hull[0], hull[mid], dot) < 0:
            end = mid
        else:
            start = mid + 1
 
    return ccw(hull[0], hull[start - 1], dot) < 0 or ccw(hull[start - 1], hull[start], dot) < 0 or ccw(hull[start], hull[0], dot) < 0
 
def find_hull(dots: list, ns: int) -> list:
    dots.sort()
    # 아직 식별하지 않은 나사 기둥 수
    remains = ns
    # 식별한 나사기둥 추적
    hull_used = [False for _i in range(ns)]
    # 나사기둥 목록
    hull: list[list[int]] = [[]]
    peek = 1
 
    while True:
        hull.append([])
 
        # 찾은 도형이 직선인지 확인하는데 사용하는 플래그
        # ccw > 0 인 세 점이 있다면 False로 설정
        is_line = True
 
        # 볼록껍질의 아래 파트
        for i in range(ns):
            if hull_used[dots[i][2]]:
                continue
            while len(hull[peek]) > 1:
                _ccw = ccw(hull[peek][-2], hull[peek][-1], dots[i])
                if _ccw > 0:
                    is_line = False
                if _ccw >= 0:
                    break
                hull[peek].pop()
            hull[peek].append(dots[i])
        hull[peek].pop()
 
        # 볼록껍질의 위 파트
        for i in range(ns - 1, -1, -1):
            if hull_used[dots[i][2]]:
                continue
            while len(hull[peek]) > 1:
                _ccw = ccw(hull[peek][-2], hull[peek][-1], dots[i])
                if _ccw > 0:
                    is_line = False
                if _ccw >= 0:
                    break
                hull[peek].pop()
            hull[peek].append(dots[i])
        hull[peek].pop()
 
        for i in range(len(hull[peek])):
            hull_used[hull[peek][i][2]] = True
        remains -= len(hull[peek])
       
        # 껍질 결과가 직선이면, 더 이상 어떻게 처리하든 직선밖에 나오지 않음
        if is_line:
            break
        # 껍질은 3개 이상의 나사구멍으로만 만들 수 있음
        if remains < 3:
            break
        
        peek += 1
 
    return hull
 
wpdp = []
def waterproof(a: int, b: int, c: int, m: int, i: int) -> int:
    global wpdp
 
    if len(wpdp) == 0:
        wpdp.append(b)
 
    if len(wpdp) < i + 1:
        wpdp.append((a * waterproof(a, b, c, m, i - 1) + c) % m)
 
    return wpdp[i]
 
def compute(tt: int, tc: int, a: int, b: int, c: int, m: int, ns: int, nd: int, s: list, d: list) -> bool:
    '''
    :return: `True` => Phone can be reused. `False` => Cannot be reused.
    '''
 
    t = max(tt, tc)
    # for level in range(nw):
    i = 0
    hull = find_hull(s, ns)
    ln_hull = len(hull)

    # 다음 침수까지 남은 시간이 없다면 더 이상의 침수는 없음
    while True:
        '''
        * 방수 씰의 처리
          방수 씰은 모든 부품을 덮는 첫번째 씰에서부터 시작하므로
          먼저 침투한 액체가 첫번째 씰을 통과하는지 여부부터 평가
        '''
        t_diff = waterproof(a, b, c, m, i) # t: 다음 방수 씰을 뚫는데 사용할 수 있는 여유 시간
        t -= t_diff
        if t <= 0:
            break
        if i >= ln_hull:
            break

        tt -= t_diff
        tc -= t_diff
 
        i += 1
 
    '''
    tt, tc의 업데이트는 더 이상 침수가 이루어지는지 확인 후에 이루어짐
    = 이전 순간의 상태 값

    이전 순간에서 tt(변기물 닿은 시간)은 유효하면서, tc(락스물 닿은 시간)이 유효하지 않다면
    변기물이 제대로 씻겨나가지 못한것
    '''
    if tt >= 0 and tc < 0:
        return False
    
    if i >= ln_hull:
        return False

    ln_end_hull = len(hull[i])
    if ln_end_hull > 2:
        for _d in d:
            if is_outside(_d, hull[i]):
                return False
    
    return True

debug = False
 
if __name__ == '__main__' and not debug:
    tt, tc = map(int, input().split())
    a, b, c, m = map(int, input().split())
    ns, nd = map(int, input().split())
    s = [[*map(int, input().split()), i] for i in range(ns)]
    d = [[*map(int, input().split())] for _i in range(nd)]
    print('Your Apple ID was used to sign in to iCloud' if compute(tt, tc, a, b, c, m, ns, nd, s, d) else 'Your purchases from Apple')
    '''
    import cProfile
    cProfile.run("print('Your Apple ID was used to sign in to iCloud' if compute(tt, tc, a, b, c, m, ns, nd, s, d) else 'Your purchases from Apple')")
    '''
    
 
if debug:
    print(ccw((0, 0), (0, 1), (0, 2)))
    print(ccw((0, 0), (2, 0), (0, 2)))
    print(is_outside((0, 1), [(0, 0), (2, 0), (0, 2)]))
