import image

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        new_red = 0.2125 * p.getRed()
        green = 0.2154 * p.getGreen()
        blue = 0.1 * p.getBlue()

        new_pixel = image.Pixel(new_red, green, blue)

        new_img.setPixel(col, row, new_pixel)

new_img.draw(win)
win.exitonclick()

