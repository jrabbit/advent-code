import ast

def main(data):
    in_mem = 0
    in_code = 0
    for line in data:
        l = line.strip() #remove newlines
        # char_s = len(l.strip('"'))
        code = len(ast.literal_eval(l))
        in_mem += len(l)
        in_code += code
    return  in_mem - in_code

def part2(data):
    in_orig = 0
    in_repr = 0
    for line in data:
        l = line.strip() #remove newlines
        # this doesn't work why?
        code = len(l)+l.count('\\')+2+l.count(r'"') # Python auto wraps in '' which isn't counted
        # print(l.count('\\'), l.count(r'"'),l.count(r'\\'))
        in_orig += len(l)
        in_repr += code
    return  in_repr - in_orig

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
        print(main(data))
        print(part2(data))