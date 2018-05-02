import image
import sys

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(0, img.getWidth()):
    for j in range(0, img.getHeight()):
        old_p = img.getPixel(i, j)
        red = old_p.getRed()
        new_p = image.Pixel(red, 0, 0)
        new_img.setPixel(i, j, new_p)

new_img.draw(win)
win.exitonclick()

