class Must_read:
    def file_reader():
        with open('data.csv', 'r') as file1:
            return (file1.read())

if __name__ == '__main__':
    print(Must_read.file_reader())