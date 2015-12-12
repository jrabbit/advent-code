import json
from compiler.ast import flatten

def hook(item):
    inp = item.values()
    return inp

def main(data):
    count = []
    for item in flatten(json.loads(data, object_hook=hook)):
        if isinstance(item, int):
            count.append(item)
    return sum(count)


if __name__ == '__main__':
    data = open("input.txt").read()
    print(main(data))