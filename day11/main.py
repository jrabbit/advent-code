
next_d = {"a": "b",
          "b": "c",
          "c": "d",
          "d": "e",
          "e": "f",
          "f": "g",
          "g": "h",
          "h": "j", # no i
          "j": "k",
          "k": "m", # no l
          "m": "n",
          "n": "p", # no o
          "p": "q",
          "q": "r",
          "r": "s",
          "s": "t",
          "t": "u",
          "u": "v",
          "v": "w",
          "w": "x",
          "x": "y",
          "y": "z",
          "z": "a"}

def validator(password):
    if 'i' in password or 'l' in password or 'o' in password:
        return False

def main(inp):
    pass

if __name__ == '__main__':
    print(main("hepxcrrq"))
