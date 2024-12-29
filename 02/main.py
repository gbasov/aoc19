with open('input.txt', encoding='ascii') as file:
    inp = [int(x) for x in file.readline().strip().split(',')]


def run(arg):
    prg = inp[:]
    prg[1:3] = arg
    p = 0
    while prg[p] != 99:
        op, pos_a, pos_b, w = prg[p:p + 4]
        a, b = prg[pos_a], prg[pos_b]
        p += 4
        match op:
            case 1:
                prg[w] = a + b
            case 2:
                prg[w] = a * b
    return prg[0]


print('Part 1:', run((12, 2)))

target = 19690720
low, high, mid = 0, 9999, 5000

while (val := run(divmod(mid, 100))) != target:
    if val < target:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

print('Part 2:', mid)
