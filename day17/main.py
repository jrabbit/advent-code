import itertools

def main(data, target=150):
    data = map(int, data)
    possibilities = []
    for r in range(len(data)):
        possibilities += [x for x in itertools.combinations(data, r)]
    return [x for x in itertools.ifilter(lambda x: sum(x) == target, possibilities)]

def part2(data, target=150):
    l = main(data, target)
    z = len(l[0])
    return filter(lambda x: len(x) == z, l)

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    print(len(main(data)))
    print(len(part2(data)))
