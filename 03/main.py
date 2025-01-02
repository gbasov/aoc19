from math import inf

wires = []
with open('input.txt', encoding='ascii') as file:
    for line in file:
        wires.append(
            [(str(s[:1]), int(s[1:])) for s in line.strip().split(',')]
        )
w1, w2 = wires

steps = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}


def traverse(wire: list[tuple[str, int]]):
    point = (0, 0)
    steps_cnt = 0
    for leg_direction, leg_len in wire:
        for i in range(leg_len):
            steps_cnt += 1
            dy, dx = steps[leg_direction]
            point = (point[0] + dy, point[1] + dx)
            yield point, leg_direction, steps_cnt


w1_path: dict[tuple[int, int], tuple[str, int]] = {}
for p, direction, path_len in traverse(w1):
    if p not in w1_path:
        w1_path[p] = (direction, path_len)

min_dist, min_delay = inf, inf
for p, direction, path_len in traverse(w2):
    if p in w1_path and w1_path[p][0] != direction:
        dist = abs(p[0]) + abs(p[1])
        min_dist = min(dist, min_dist)
        delay = w1_path[p][1] + path_len
        min_delay = min(delay, min_delay)

print(min_dist)
print(min_delay)
