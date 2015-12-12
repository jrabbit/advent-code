import re
PATTERN = re.compile(ur'((\d)(?:\2+)?)') #thanks #regex


def breakdown(s):
    return [x[0] for x in re.findall(PATTERN, s)]

def str_count(i, count):
    return str(str(i).count(str(count)))

def main(start="1113222113", steps=40):
    current = start
    while steps > 0:
        def f(current):
            ret =  ""
            # print "got current", current
            for group in breakdown(current):
                comp = str(len(group))+group[0]
                # print "comp", comp
                ret += comp
            return ret
        # current = str_count(current,count)+current
        current = f(current)
        # print current
        steps -= 1
    return len(current)


if __name__ == '__main__':
    print(main())
    print(main(steps=50))