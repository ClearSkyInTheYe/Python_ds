#
# def to_int(a):
#     x = int(a)
#     return ix)

def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    dict1 = dict(list_of_tuples)
    dict1s = dict(sorted(dict1.items()))
    dict2s = dict(sorted(dict1s.items(), key=lambda item: -int(item[1])))
    # dict2s = dict(sorted(dict1s.items(), key=to_int(dict1.keys())))
    inv_dict = {value: key for key, value in dict2s.items()}
    for key, value in inv_dict.items():
        print(inv_dict[key])

if __name__ == '__main__':
    data()
