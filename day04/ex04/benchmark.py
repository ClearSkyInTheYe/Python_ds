import timeit
from random import randint
from collections import Counter

def m_f(lst):
    dict1 = {}
    for e in lst:
        if e not in dict1:
            dict1[e] = 1
        else:
            dict1[e] += 1
    return dict1

def my_top(lst):
    dict1 = m_f(lst)
    s_list = sorted(dict1.items(), key=lambda item: -int(item[1]))
    top_list = s_list[:10]
    return dict((x, y) for x, y in top_list)


def counter_dict(list):
    return dict(Counter(list))

def counter_top_10(list):
    return Counter(list).most_common(10)

def bench():
    lst = [randint(0, 100) for i in range(100000)]
    print('my function:', timeit.timeit(f'm_f({lst})',
                                        number=1,
                                        setup='from __main__ import m_f'))
    print('Counter:', timeit.timeit(f'counter_dict({lst})',
                                    number=1,
                                    setup='from __main__ import counter_dict'))
    print('my top:', timeit.timeit(f'my_top({lst})',
                                   number=1,
                                   setup='from __main__ import my_top'))
    print("Counter's top:", timeit.timeit(f'counter_top_10({lst})',
                                          number=1,
                                          setup='from __main__ import counter_top_10'))

if __name__ == '__main__':
    bench()