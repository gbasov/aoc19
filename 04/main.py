from time import time

start = time()
with open('input.txt') as file:
    str_low, str_high = file.readline().strip().split('-')

num_low, num_high = int(str_low), int(str_high)
seq_low, seq_high = (list(map(int, num)) for num in (str_low, str_high))
seq_len = len(seq_low)


def is_valid(seq: list[int]):
    prev = 0
    repeated = 0
    at_least, exact = 0, 0
    for n in seq + [None]:
        if n == prev:
            at_least = 1
            repeated += 1
        else:
            if repeated == 2:
                exact = 1
            repeated = 1
        prev = n

    if at_least and in_range(seq):
        return at_least, exact

    return 0, 0


def in_range(seq: list[int]):
    num = int(''.join(map(str, seq)))
    return num_low <= num <= num_high


def find(seq: list[int]) -> tuple[int, int]:
    if len(seq) == seq_len:
        return is_valid(seq)

    if seq:
        low, high = seq[-1], 9
    else:
        low, high = seq_low[0], seq_high[0]

    sum1, sum2 = 0, 0
    for i in range(low, high + 1):
        valid1, valid2 = find(seq + [i])
        sum1 += valid1
        sum2 += valid2

    return sum1, sum2


print(find([]))

exec_time = (time() - start) * 1000
print(f'Time {exec_time:.3f}ms')
