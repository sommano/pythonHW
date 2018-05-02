import image

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        new_red = (p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        green = (p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        blue = (p.getRed() * 0.272 + p.getGreen() *0.543 + p.getBlue() * 0.131)

        new_pixel = image.Pixel(new_red, green, blue)

        new_img.setPixel(col, row, new_pixel)

new_img.draw(win)
win.exitonclick()





