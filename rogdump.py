"""

R.o.G.
Datafile Dump

"""

import shelve
import sys


def main():
    if len(sys.argv) != 2:
        print("Use: python rogdump.py \"my_dump.file\"")
        exit(1)
    else:
        data = shelve.open(sys.argv[1])
        keys_in_data = list(data.keys())
        keys_in_data.sort()
        for data_key in keys_in_data:
            print(str(data_key) + ": " + str(data[data_key]))
        data.close()


if __name__ == '__main__':
    main()
