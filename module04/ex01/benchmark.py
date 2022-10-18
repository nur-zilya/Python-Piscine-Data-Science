import timeit

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

def main():
    n = 900000
    loop_time = timeit.timeit('loop_approach()', 'from __main__ import loop_approach', number=n)

    compr_time = timeit.timeit('list_comprehension()', 'from __main__ import list_comprehension', number=n)

    map_time = timeit.timeit('map_list()', 'from __main__ import map_list', number=n)

    if loop_time > compr_time and map_time > compr_time:
        print('it is better to use a list comprehension')
    elif loop_time > map_time and compr_time > map_time:
        print('it is better to use a map')
    else:
        print('it is better to use a loop')

    print(*sorted([loop_time, compr_time, map_time]), sep=' vs ')

if __name__ == "__main__":
    main()

