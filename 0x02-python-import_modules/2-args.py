#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 1
    ac = len(sys.argv) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(ac))
        for arg in sys.argv:
            if counter <= ac:
                print("{:d}: {}".format(counter, sys.argv[counter]))
                counter += 1
            else:
                break
