import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
emails = emails * 5

def cycle():
    a = []
    for e in emails:
        if e.find("@gmail.com") > 0:
            a.append(e)
    return a

def compr():
    a = [element for element in emails if element.find('@gmail.com') > 0]
    return a

def is_in(x):
    if '@gmail.com' in x:
        return x

def withmap():
    new_emails = map(is_in, emails)
    return new_emails

def withfilter():
    new_emails = filter(is_in, emails)
    return list(new_emails)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception("argument error")
    x = int(sys.argv[2])
    if sys.argv[1] == 'map':
        print(timeit.timeit(withmap, number=x))
    if sys.argv[1] == 'list_comprehension':
        print(timeit.timeit(compr, number=x))
    if sys.argv[1] == 'loop':
        print(timeit.timeit(cycle, number=x))
    if sys.argv[1] == 'filter':
        print(timeit.timeit(withfilter, number=x))
