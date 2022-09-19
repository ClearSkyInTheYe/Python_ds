import sys
from random import randint

class Research:
    fil_name: str

    def __init__(self, name):
        self.fil_name = name

    def file_reader(self, has_header = True):
        a = {'0,1\n', '1,0\n', '0,1', '1,0'}
        with open(self.fil_name, 'r') as file1:
            s = file1.readlines()
        file1.close()
        if s[0] == '0,1\n':
            has_header = False
        if len(s[0].split(',')) != 2 and has_header == True:
            raise Exception('Error: wrong header')
        sf = s[0].split(',')
        if len(sf[0]) == 0 or sf[1] == '\n' and has_header == True:
            raise Exception('Error: wrong header')
        lst = []
        for n in range(len(s)):
            if len(s[n].split(',')) != 2:
                raise Exception('Error: wrong data')
            if s[n] not in a and n != 0:
                raise Exception('Error: wrong data')
        for n in range(len(s)):
            if has_header == True:
                n += 1
                if n >= len(s):
                    break
            f = int(s[n][0])
            b = int(s[n][2])
            lst1 = [f, b]
            lst.append(lst1)
        return lst

    class Calculations:
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            h = 0
            t = 0
            for n in range(len(self.data)):
                if self.data[n][0] == 1:
                    h += 1
                else:
                    t += 1
            return h, t

        def fractions(self):
            a = self.count[0] + self.count[1]
            x = self.count[0] / a
            v = self.count[1] / a
            return (x * 100, v * 100)

    class Analytics(Calculations):
        def __init__(self, n_steps):
            self.n_steps = n_steps
            self.predict = self.predict_random()
            self.predict_last = self.predict_last()

        def predict_random(self):
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(self.n_steps)]

        def predict_last(self):
            return self.predict[-1]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Error argument")
    a = Research(sys.argv[1]).file_reader()
    x = Research.Calculations(a)
    pr = Research.Analytics(3)
    f = Research.Calculations.fractions(x)
    print(x.data)
    print(x.count[0], x.count[1])
    print(round(f[0], 2), round(f[1], 2))
    print(pr.predict)
    print(pr.predict_last)
