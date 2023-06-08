#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_sum = 0
    for i in range(1, len(sys.argv)):
        sys.argv[i] = int(sys.argv[i])
        total_sum += sys.argv[i]

    print(total_sum)
