import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
emails = emails * 5

def cycle():
    a = []
    for e in emails:
        if e.find("@gmail.com"):
            a.append(e)
    return a

def compr():
    a = [element for element in emails if element.find('@gmail.com') > 0]
    return a


if __name__ == '__main__':
    time1 = timeit.timeit(cycle, number = 9 * 10 ** 7)
    time2 = timeit.timeit(compr, number=9 * 10 ** 7)
    if time1 < time2:
        print('it is better to use a loop')
        print(time1, 'vs', time2)
    else:
        print('it is better to use a list comprehension')
        print(time2, 'vs', time1)