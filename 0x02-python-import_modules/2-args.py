#!/usr/bin/python3
import sys
elements = sys.argv
count = len(sys.argv)
rcount = count - 1

if __name__ == "__main__":
    if rcount == 1:
        print(f"1 argument:")
        for a in range(1, 2):
            print(f"{a}: {elements[a]}")

    elif rcount > 1:
        print(f"{rcount} arguments:")
        for a in range(1, count):
            print(f"{a}: {elements[a]}")

    else:
        print(f"0 arguments.")
