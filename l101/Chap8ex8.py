import image

def convert_black_white(input_image):
    grayscale_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            original_pixel = input_image.getPixel(col, row)

            red = original_pixel.getRed()
            green = original_pixel.getGreen()
            blue = original_pixel.getBlue()

            avg = (red + green + blue) / 3.0

            new_pixel = image.Pixel(avg, avg, avg)
            grayscale_image.setPixel(col, row, new_pixel)

    black_white_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            original_pixel = grayscale_image.getPixel(col, row)
            red = original_pixel.getRed()
            if red > 140:
                val = 255
            else:
                val = 0

            new_pixel = image.Pixel(val, val, val)
            black_white_image.setPixel(col, row, new_pixel)
    return black_white_image

def main():
    img = image.Image("luther.jpg")
    win = image.ImageWin(img.getWidth(), img.getHeight())

    bw_img = convert_black_white(img)
    bw_img.draw(win)

    win.exitonclick()

if __name__ == "__main__":
    main()

