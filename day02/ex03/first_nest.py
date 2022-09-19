import sys
import os

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

        def counts(self, list_lists):
            h = 0
            t = 0
            for n in range(len(list_lists)):
                if list_lists[n][0] == 1:
                    h += 1
                else:
                    t += 1
            return h, t

        def fractions(self, list_c):
            a = list_c[0] + list_c[1]
            x = list_c[0] / a
            v = list_c[1] / a
            return (x * 100, v * 100)




if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Error argument")
    a = Research(sys.argv[1])
    lst = a.file_reader()
    print(a.file_reader())
    b = Research.Calculations()
    lsct_c = b.counts(lst)
    f = b.fractions(lsct_c)
    print(lsct_c[0], lsct_c[1])
    print(f[0], f[1])