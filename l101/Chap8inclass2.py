import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel
        #random.randint(i - 1, i + 1)
        #random.randint(j - 1, j + 1)

        p = img.getPixel(((random.randrange(-1, 2, 2)) + i), ((random.randrange(-1, 2, 2)) + j))

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        # TODO: in the new image, set this pixel's color to the neighbor's color
        new_p = image.Pixel(red, green, blue)
        new_img.setPixel(i, j, new_p)

new_img.draw(win)
win.exitonclick()

