def setup():
    img = loadImage('http://i.huffpost.com/gen/2214266/thumbs/o-WOMAN-YELLING-facebook.jpg')
    size(img.width, img.height)
    colorMode(HSB)
    noStroke()
    image(img, 0, 0)
    filter(GRAY)
    grid(2, 35, 10)


def draw():
    pass


def grid(res, move, strength):
    #colorbars
    loadPixels()
    clrSwitch = True
    for x in range(0, width, res * 2):
        if clrSwitch == True:
            clr = 0
            clrSwitch = not clrSwitch
        else:
            clr = 125
            clrSwitch = not clrSwitch
        for y in range(0, height, res):
            c = getContrast(x, y, res)
            fill(clr, 255, c * strength, c * strength * 2)
            noStroke()
            rect(x, y, res, res)
    #move pixels
    for x in range(0, width, res):
        copy(x, 0, res, height, x, int(random(-1*move, move)), res, height)


def getContrast(x, y, res):
    lumA = getLum(x, y, res)
    lum1 = getLum(x - res, y, res)
    lum2 = getLum(x + res, y, res)
    lum3 = getLum(x, y - res, res)
    lum4 = getLum(x, y + res, res)
    lum5 = getLum(x - res, y - res, res)
    lum6 = getLum(x + res, y - res, res)
    lum7 = getLum(x + res, y + res, res)
    lum8 = getLum(x - res, y + res, res)
    c1 = abs(lumA - lum1)
    c2 = abs(lumA - lum2)
    c3 = abs(lumA - lum3)
    c4 = abs(lumA - lum4)
    c5 = abs(lumA - lum5)
    c6 = abs(lumA - lum6)
    c7 = abs(lumA - lum7)
    c8 = abs(lumA - lum8)
    return (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8) / 8


def getLum(x, y, res):
    lumsum = 0
    for brx in range(res):
        for bry in range(res):
            try:
                c = color(pixels[(y + bry) * width + (x + brx)])
                r = c >> 16 & 0xFF
                g = c >> 8 & 0xFF
                b = c & 0xFF
                lum = (0.299 * r + 0.587 * g + 0.114 * b)
                lumsum += lum
            except:
                pass
    return lumsum / (res * res)
