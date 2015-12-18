
class AuntSue(object):
    """describes the things"""
    def __init__(self, number, children=None, cats=None, samoyeds=None, 
                 pomeranians=None, akitas=None, vizslas=None, goldfish=None,
                 trees=None, cars=None, perfumes=None):
        super(AuntSue, self).__init__()
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes
    def __repr__(self):
        return self.number


def main(data):
    sues = []
    for i in data:
        name = i.split(":",1)[0]
        values = i.split(":",1)[1].strip().split(', ')
        props = {}
        for item in values:
            props[item.split(":")[0]] = int(item.split(":")[1])
        sues.append(AuntSue(name, **props))
    print(sues)



if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    print(main(data))
