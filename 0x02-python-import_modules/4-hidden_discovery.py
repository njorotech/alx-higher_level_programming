#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    first_letter = '_'
    for name in dir(hidden_4):
        if (name[0] != first_letter) and (name[1] != first_letter):
            print(name)
