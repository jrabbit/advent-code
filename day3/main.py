# from collections import namedtuple

# Coordinate = namedtuple('Coordinate', ['x', 'y'])

class Coordinate(object):
    def __init__(self, x, y):
        super(Coordinate, self).__init__()
        self.x = x
        self.y = y
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    def __repr__(self):
        return "[%s, %s]" % (self.x, self.y)
        
def main(data):
    position = Coordinate(0,0)
    presents = {Coordinate(0,0)}
    for char in data:
        if char == "^":
            position.y += 1
        elif char == "v":
            position.y -= 1
        elif char == ">":
            position.x += 1
        elif char == "<":
            position.x -= 1
        # print position
        presents.add((position.x, position.y))
        # can't add position because we keep changing it!
        # print presents
    print position
    print len(presents)



def part2(data):
    pass

if __name__ == '__main__':
    data = open("input.txt").read()
    main(data)
    part2(data)