
def main(data):
    total =0
    for l in data.split():
        l,w,h = l.split('x')
        l,w,h = int(l), int(w), int(h)
        side1 = l*w
        side2 = w*h
        side3 = h*l
        slack = min(side1, side2, side3)
        sa = 2*l*w + 2*w*h + 2*h*l
        total += slack + sa
    print total

if __name__ == '__main__':
    data = open("input.txt").read()
    main(data)
    # part2(data)