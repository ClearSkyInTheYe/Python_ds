def read_and_write(f_name):
    file1 = open(f_name + '.csv', 'r')
    file2 = open(f_name + '.tsv', 'w')
    file2.write(file1.read().replace(',', '\t'))

if __name__ == '__main__':
    read_and_write('hh')