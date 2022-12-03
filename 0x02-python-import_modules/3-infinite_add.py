#!/usr/bin/python3
import sys
numbers = sys.argv
count = len(numbers)
total = 0

if __name__ == "__main__":
    for a in range(1, count):
        total += int(numbers[a])

    print(f"{total}")
