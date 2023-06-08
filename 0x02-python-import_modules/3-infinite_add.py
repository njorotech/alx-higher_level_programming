#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    ac = len(argv)
    total = 0
    counter = 1
    if ac > 1:
        for arg in argv:
            if counter < ac:
                total += int(argv[counter])
                counter += 1
            else:
                break
    print(total)
