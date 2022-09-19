import os
import sys

class Research:
    fil_name: str
    def __init__(self, name):
        self.fil_name = name
    def file_reader(self):
        a = {'0,1\n', '1,0\n', '0,1', '1,0'}
        with open(self.fil_name, 'r') as file1:
            s = file1.readlines()
        file1.close()
        if s[0] == '0,1\n':
            raise Exception('Error: file without header')
        if len(s[0].split(',')) != 2:
            raise Exception('Error: wrong header')
        sf = s[0].split(',')
        if len(sf[0]) == 0 or sf[1] == '\n':
            raise Exception('Error: wrong header')
        for n in range(len(s)):
            if len(s[n].split(',')) != 2:
                raise Exception('Error: wrong data')
            if s[n] not in a and n != 0:
                raise Exception('Error: wrong data')
        with open(self.fil_name, 'r') as file2:
            x = file2.read()
        file2.close()
        return x


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Error argument")
    a = Research(sys.argv[1])
    print(a.file_reader())
