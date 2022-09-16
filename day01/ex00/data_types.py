def data_types():
    a = 0
    b = 'str'
    c = 0.0
    d = True
    e = ['1', '2']
    f = {}
    g = ('a', 2, True)
    h = set(g)
    s = ","
    print("[", type(a).__name__, s, type(b).__name__, s,  type(c).__name__, s,  type(d).__name__, s,
          type(e).__name__, s,  type(f).__name__, s,  type(g).__name__, s, type(h).__name__, "]")


if __name__ == '__main__':
    data_types()