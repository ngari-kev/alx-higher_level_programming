#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    index = 1

    if len(args) == 1:
        print("0 arguments")

    elif len(args) == 2:
        print("1 argument")
        print("{}: {}".format(index, args[1]))
    else:
        args = sys.argv[1:]
        print("{} arguments".format(len(args)))
        for arg in args:
            print("{}: {}".format(index, arg))
            index += 1
