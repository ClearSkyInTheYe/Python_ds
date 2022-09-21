import timeit
import sys
from functools import reduce

def cycle(x):
    i = 0
    for n in range(x + 1):
        i += n * n
    return i


def sum_it(prev, current):
    return (prev + current ** 2)

def red(n):
    sum = reduce(sum_it, range(x + 1))
    # sum = reduce(lambda y, x: y + x ** 2, range(1, n + 1))
    return sum
    # return reduce(lambda x, y: x + y ** 2, lst)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("argument error")
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    if sys.argv[1] == 'loop':
        print(timeit.timeit(lambda: cycle(int(sys.argv[3])), number=int(sys.argv[2])))
    elif sys.argv[1] == 'reduce':
        print(timeit.timeit(lambda: red(int(sys.argv[3])), number=int(sys.argv[2])))