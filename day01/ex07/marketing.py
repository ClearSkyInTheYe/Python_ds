import sys

def inv(a, b):
    v = set(a)
    x = set(b)
    return list(v - x)

def inv1(a, b):
    v = set(a)
    x = set(b)
    return list(v - x)

def inv2(a, b):
    v = set(a)
    x = set(b)
    return list(v - x)

def marketing(s):
    cclients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
                     'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if s == 'potential_clients':
        pc = inv2(participants, cclients)
        print(pc)
        return
    elif s == 'call_center':
        pc = inv(cclients, recipients)
        print(pc)
        return
    elif s == 'loyalty_program':
        pc = inv1(cclients, participants)
        print(pc)
        return
    print("Error argument")

if __name__ == '__main__':
    if len(sys.argv) != 2 or (sys.argv[1] != 'call_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
        raise Exception("Error argument")
    marketing(sys.argv[1])
