import sys
import timeit
from functools import reduce

def get_n():
    if sys.argv[3].isdigit():
        return int(sys.argv[3])

def sum_of_squares(n : int = get_n()):
    res = 0
    for i in range(1, n + 1):
        res += i ** 2
    return res

def reduce_sqrt_sum(n : int = get_n()):
    def func(x, y):
        return x + y * y
    return reduce(func, range(1, n + 1))

def main():
    dictionary = {'loop': 'sum_of_squares',
                 'reduce': 'reduce_sqrt_sum'}

    if sys.argv[1] in dictionary and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        time = timeit.timeit(f'{dictionary[sys.argv[1]]}()',
                                f'from __main__ import {dictionary[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time)
    else:
        print('Bad Arg')

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()

