"""

R.o.G.
Editor

"""

import shelve

world = shelve.open("data\\world.map")


def set_origin():
    world["origin"] = {'x': 0.0, 'y': 0.0}


def quit_edit():
    world.close()


def main():
    try:
        set_origin()
    finally:
        quit_edit()


if __name__ == "__main__":
    main()
