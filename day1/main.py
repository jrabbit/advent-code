

def main(data):
    print len([x for x in data if x == "("]) - len([x for x in data if x == ")"])

if __name__ == '__main__':
    data = open("input.txt").read()
    main(data)