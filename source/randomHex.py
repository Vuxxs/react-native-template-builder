from random import randint

# https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python/18035471


def getRandomHexColor():
    def r(): return randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())
