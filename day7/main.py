class Instruction(object):
    pass


def main(data):
    # [{q.split('->')} for q in data]
    # f = []
    # for instruction in data:
    x = [q.split('->') for q in data]
    p = {q[-1].strip(): q[0] for q in x}
    start = p['a']
    def f(key):
        x = p[key].strip()
        print x
        f(x)
    f("a")


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    main(data)