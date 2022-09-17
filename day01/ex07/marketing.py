import sys

def inv(a, b):
    v = set(a)
    x = set(b)
    f = []
    for n in v:
        if n not in x:
            f.append(n)
    return f

def marketing(s):
    cclients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
                     'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    # pc = []
    # lc = []
    # x = []
    d = participants + cclients
    # pc = inv(cclients, participants)
    # print(pc)
    # for n in range(len(participants)):
    #     if participants[n] not in cclients:
    #         lc.append(participants[n])
    # for n in range(len(d)):
    #     if d[n] not in recipients :
    #         x.append(d[n])
    if s == 'potential_clients':
        pc = inv(participants, cclients)
        print(pc)
        return
    elif s == 'call_center':
        pc = inv(d, recipients)
        print(pc)
        return
    elif s == 'loyalty_program':
        pc = inv(cclients, participants)
        print(pc)
        return
    print("Error argument")

if __name__ == '__main__':
    if len(sys.argv) == 2:
       marketing(sys.argv[1])
