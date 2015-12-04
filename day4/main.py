import hashlib

def incrementer(seq=0):
    while True:
        yield seq
        seq += 1



def main(secret_key):
    advent_coin = "00000"
    for sequence in incrementer(0):
        md5 = hashlib.md5()
        md5.update(secret_key+str(sequence))
        digest = md5.hexdigest()
        # print digest
        if digest[:5] == advent_coin:
            print sequence
            print digest
            break

def main2(secret_key, digits=6):
    advent_coin = "0" * digits
    for sequence in incrementer(0):
        md5 = hashlib.md5()
        md5.update(secret_key+str(sequence))
        digest = md5.hexdigest()
        # print digest
        if digest[:digits] == advent_coin:
            print sequence
            print digest
            break


if __name__ == '__main__':
    main2("bgvyzdsv", digits=5)
    main2("bgvyzdsv", digits=6)