import re
import itertools

def is_nice(s):
    for pair in ["ab","cd","pq", "xy"]:
        if pair in s:
            # It does not contain the strings ab, cd, pq, or xy
            return False
    v = 0
    vowels = [x for x in "aeiou"]
    for letter in s:
        if letter in vowels:
            v += 1
    if v < 3:
        # It contains at least three vowels
        return False
    z = [y for y in [list(x) for q, x in itertools.groupby(s)] if len(y) >1]
    # print z
    if len(z) < 1:
        return False

    # none of the tests fail
    return True

def is_nice2(s):
    # Not my regex.
    pattern = re.compile(ur'([a-z]{2}).*\1')
    pattern2 = re.compile(r'([a-z]).(\1)')
    #end not my regex
    if pattern.search(s) and pattern2.search(s):
        return True
    else:
        return False


def main(data):
    # naughty = 0
    nice = 0
    for l in data:
        if is_nice(l):
            # print l
            nice += 1
        else:
            pass
            # print "naughty"
    return nice

def part2(data):
    nice = 0
    for l in data:
        if is_nice2(l):
            # print l
            nice += 1
        else:
            pass
            # print "naughty"
    return nice

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    print main(data)
    print part2(data)