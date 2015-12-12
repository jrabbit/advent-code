import re

def breakdown(s):
    p = re.compile(ur'((\d)(?:\2+)?)') #thanks #regex
    return [x[0] for x in re.findall(p, s)]

def str_count(i, count):
    return str(str(i).count(str(count)))

def main(start="1113222113", steps=40):
    current = start
    while steps > 1:
        # if 40 - steps > 9:
        #     count = 9
        # else:
        #     count = 40 - steps
        # str_count(current, count)
        def f(current):
            ret =  ""
            print current
            for group in breakdown(current):
                ret += str(len(group))+group[0]
            return f(ret)
        # current = str_count(current,count)+current
        current = f(current)
        print current
        steps -= 1


if __name__ == '__main__':
    print(main())