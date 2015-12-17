import itertools

def main(data):
    data = map(int, data)
    possibilities = []
    for r in range(len(data)):
        possibilities += [x for x in itertools.combinations(data, r)]
    return len([x for x in itertools.ifilter(lambda x: sum(x) == 150, possibilities)])

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    print(main(data))
