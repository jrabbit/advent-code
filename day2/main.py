
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

def part2(data):
    total =0
    for l in data.split():
        l,w,h = l.split('x')
        l,w,h = int(l), int(w), int(h)
        side1 = l*2+w*2
        side2 = w*2+h*2
        side3 = h*2+l*2
        # sides = [{"dimensions": (l,w),"perimeter": l*2+w*2}, 
        #          {"dimensions": (w,h),"perimeter": w*2+h*2},
        #          {"dimensions": (h,l),"perimeter": h*2+l*2}
        #         ]
        small_perimeter = min(side1, side2, side3)
        # sa = 2*l*w + 2*w*h + 2*h*l
        volume = l*w*h
        total += volume + small_perimeter
    print total
if __name__ == '__main__':
    data = open("input.txt").read()
    main(data)
    part2(data)