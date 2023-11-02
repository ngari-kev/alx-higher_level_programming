#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if not args:
        print("0 arguments")
    else:
        print("{} argument{}".format(len(args), 's' if len(args) > 1 else ''))
        for index, arg in enumerate(args, start=1):
            print("{}: {}".format(index, arg))
