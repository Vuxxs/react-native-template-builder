import random


def getRandomAlignment():
    alignments = ["'center'", "'flex-end'", "'flex-start'", "'stretch'"]
    return alignments[random.randrange(len(alignments))]


# https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python/18035471
def getRandomHexColor():
    def r(): return random.randint(0, 255)
    return "'#%02X%02X%02X'" % (r(), r(), r())


def makeComponent(key):
    if(key.startswith("bu")):
        return ''
    elif(key.startswith("im")):
        randomWH = random.sample(range(49, 201), 2)
        return "\t" + key + """: {
        width: """ + str(randomWH[0]) + """,
        height: """ + str(randomWH[1]) + """,
        alignSelf: """ + getRandomAlignment() + """
    },\n\n"""
    elif(key.startswith("pr")):
        return "\t" + key + """: {
        backgroundColor: """ + getRandomHexColor() + """
    },\n\n"""
    elif(key.startswith("sw")):
        return "\t" + key + """: {
        alignSelf: """ + getRandomAlignment() + """
    },\n\n"""
    elif(key.startswith("te")):
        return "\t" + key + """: {
        fontSize: """ + str(random.randint(12, 26)) + """,
        fontWeight: 'bold',
        alignSelf: """ + getRandomAlignment() + """
    },\n\n"""
    elif(key.startswith("ti")):
        return "\t" + key + """: {
        backgroundColor: """ + getRandomHexColor() + """,
        alignSelf: """ + getRandomAlignment() + """
    },\n\n"""


def makeStylesheet(key):
    f = open("./templates/Stylesheets/Random", "a")
    f.write(makeComponent(key))
    f.close()
