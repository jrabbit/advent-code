

def main(data):
    print len([x for x in data if x == "("]) - len([x for x in data if x == ")"])

def part2(data):
    count = 0
    for position, x in enumerate(data):
        if x == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            print position +1
            break

if __name__ == '__main__':
    data = open("input.txt").read()
    main(data)
    part2(data)