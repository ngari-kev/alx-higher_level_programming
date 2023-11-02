#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    index = 1

    if not args:
        print("0 arguments")
    else:
        print("{} argument{}".format(len(args), 's' if len(args) > 1 else ''))
        for arg in args:
            print("{}: {}".format(index, arg))
            index += 1
