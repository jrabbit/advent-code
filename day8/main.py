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
    print  in_mem - in_code

def part2(data):
    in_orig = 0
    in_repr = 0
    for line in data:
        l = line.strip() #remove newlines
        code = len(repr(l))+2 # Python auto wraps in '' which isn't counted
        in_orig += len(l)
        in_repr += code
    print  in_repr - in_orig

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
        main(data)
        part2(data)