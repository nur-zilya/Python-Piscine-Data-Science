import timeit
import sys

def get_mail_list():
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

def loop_approach(emails : list = get_mail_list()):
    new_list = []
    for e in emails:
        if e.endswith('@gmail.com'):
            new_list.append(e)
    return new_list

def list_comprehension(emails : list = get_mail_list()):
    return [e for e in emails if e.endswith('@gmail.com')]

def map_list(emails: list = get_mail_list()):
    return list(map(lambda x: x if x.endswith('@gmail.com') else None, emails))

def filter_func(emails: list = get_mail_list()):
    result = []
    def func(x):
        if x.endswith('@gmail.com'):
            return x
    return list(filter(func, emails))

def main():
    dictionary = {'list_comprehension': 'list_comprehension',
                 'loop': 'loop_approach',
                 'map': 'map_list',
                 'filter': 'filter_func'}

    if sys.argv[1] in dictionary and sys.argv[2].isdigit():
        time = timeit.timeit(f'{dictionary[sys.argv[1]]}()',
                                f'from __main__ import {dictionary[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time)
    else:
        print('wrong arguments')

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main()

