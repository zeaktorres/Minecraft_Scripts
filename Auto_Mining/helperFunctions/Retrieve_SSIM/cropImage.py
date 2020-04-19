# Opens a image in RGB mode 
def cropImage(x, y, width, height, image):

    # Cropped image of above dimension 
    # (It will not change orginal image) 
    image = image.crop((x, y, x + width, y + height)) 
    return image