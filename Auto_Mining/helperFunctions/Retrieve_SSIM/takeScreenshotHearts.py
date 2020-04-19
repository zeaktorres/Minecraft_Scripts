


from helperFunctions.Retrieve_SSIM.screenshot import takeScreenshot
from helperFunctions.Retrieve_SSIM.cropImage import cropImage
from helperFunctions.Retrieve_SSIM.compareImages import compareImages
import time


#Return value for images
def takeScreenshotHearts(i):
    #Creates tmp
    try:
        os.mkdir("./tmp")
    except:
        test = 1

    #Take screenshot and crop images  
    image = takeScreenshot()

    #Crop images
    cropImage(592, 924, 333, 43, image).save("./tmp/image%d.png" % (i))

