# based on https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent

# the Timewarp project uses 255, 0, 255 as their transparent color.
# this loads a bmp file and converts it in memory to raw pixel data.
#  we then search the pixels and convert any 255,0,255 pixels to have an
# alpha channel value of 0 and then saves the raw pixels out as a png
# file for use in the arcade engine


from PIL import Image


def convert_sprite(bmp_path, png_path):
    img = Image.open(bmp_path)
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 0, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    img.save(png_path, "PNG")


def main():
    convert_sprite("SHIP.bmp", "ship2.png")


if __name__ == "__main__":
    main()