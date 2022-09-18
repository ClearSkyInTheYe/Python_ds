import sys

def caesar(c, s, n):
    if c == 'decode':
        n *= -1
    st = ''
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(s)):
        if s[i] in alphabet1:
            m = alphabet1.find(s[i])
            st += alphabet1[(n + m) % len(alphabet1)]
        elif s[i] in alphabet2:
            m = alphabet2.find(s[i])
            s += alphabet2[(n + m) % len(alphabet2)]
        else:
            st += s[i]
        print(st)

if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception("Error argument")
    if not sys.argv[2].isascii():
        raise Exception("Error: str not from ascii")
    try:
        n_shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Error: shift is not int")
    caesar(sys.argv[1], sys.argv[2], n_shift)