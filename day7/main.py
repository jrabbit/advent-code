class Instruction(object):
    pass


def main(data, key="a"):
    # [{q.split('->')} for q in data]
    # f = []
    # for instruction in data:
    x = [q.split('->') for q in data]
    p = {q[-1].strip(): q[0] for q in x}
    start = p[key]
    def f(key):
        if key.isdigit():
            print "got value 1", key
            return int(key)
        if len(key) > 1:
            instr = key.split()
            for i in instr:
                if i.islower():
                    z = f(i)
                    print z
                    return z
        x = p[key].strip()
        print x
        f(x)
    f(key)


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    main(data)