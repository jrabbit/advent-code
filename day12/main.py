import json
import collections
from compiler.ast import flatten
# This is technically deprecated wubba lubba dub dub


def hook(item):
    inp = item.values()
    return inp


def hook2(item):
    inp = item.values()
    if "red" in inp:
        return None
    return inp


def main(data, h=hook):
    count = []
    for item in flatten(json.loads(data, object_hook=h)):
        if isinstance(item, int):
            count.append(item)
    return sum(count)


if __name__ == '__main__':
    data = open("input.txt").read()
    print(main(data))
    print(main(data, hook2))
