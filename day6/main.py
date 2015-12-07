from collections import defaultdict

def create_array(size):
    return [[False for x in range(size)] for x in range(size)] 

# def coordset(coord1, coord2):
#     coords = set()
#     x_line = coord1[0] - coord2[0]


def getCoordSetThrough(c1, c2):
    "Wholesale stolen https://gist.github.com/ubiquill/7f67294197e5226fd3fb"
    coordSet = set()
    xRange = list()
    yRange = list()
    if c1[0] <= c2[0]:
        xRange = range(c1[0], c2[0]+1)
    else:
        xRange = range(c2[0], c1[0]+1)
    if c1[1] <= c2[1]:
        yRange = range(c1[1], c2[1]+1)
    else:
        yRange = range(c2[1], c1[1]+1)
    for x in xRange:
        for y in yRange:
            c = (x, y)
            coordSet.add(c)
    return coordSet
# end steally wheely automobiley

def main(data):
    lights_on = set()
    for line in data:
        # toggle 461,550 through 564,900
        command = line.split()[-4]
        coord1 = map(int, line.split()[-3].split(','))
        coord2 = map(int, line.split()[-1].split(','))
        affected_lights = getCoordSetThrough(coord1, coord2)
        if command == "on":
            lights_on |= affected_lights
        elif command == "off":
            lights_on -= affected_lights
        elif command == "toggle":
            lights_on ^= affected_lights
    print len(lights_on)

def part2(data):
    lights_on = defaultdict(lambda: 0)
    for line in data:
        # toggle 461,550 through 564,900
        command = line.split()[-4]
        coord1 = map(int, line.split()[-3].split(','))
        coord2 = map(int, line.split()[-1].split(','))
        affected_lights = getCoordSetThrough(coord1, coord2)
        if command == "on":
            for light in affected_lights:
                lights_on[light] += 1
        elif command == "off":
            for light in affected_lights:
                if lights_on[light] == 0:
                    pass
                else:
                    lights_on[light] -= 1
        elif command == "toggle":
            for light in affected_lights:
                lights_on[light] += 2
    print sum(lights_on.values())

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    main(data)
    part2(data)
