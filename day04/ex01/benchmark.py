import timeit

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
    if x.find('@gmail.com') > 0:
        return x
    else:
        return

def withmap():
    new_emails = map(is_in, emails)
    return list(new_emails)

if __name__ == '__main__':
    time1 = timeit.timeit(cycle, number =9 * 10 ** 7)
    time2 = timeit.timeit(compr, number=9 * 10 ** 7)
    time3 = timeit.timeit(withmap, number=9 * 10 ** 7)
    times = (time1, time2, time3)
    times = sorted(times)
    if times[0] == time1:
        print('it is better to use a loop')
        print(time1, 'vs', times[1], 'vs', times[2])
    if times[0] == time2:
        print('it is better to use a list comprehension')
        print(time2, 'vs', times[1], 'vs', times[2])
    if times[0] == time3:
        print('it is better to use a map')
        print(time3, 'vs', times[1], 'vs', times[2])
