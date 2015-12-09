import networkx as nx


def get_locs(data):
    locs = set()
    for l in data:
        locs.update(l.split(' = ')[0].split(" to "))
    # locs now list of unique nodes
    return locs


def main(data):
    locs = get_locs(data)

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    print(main(data))
