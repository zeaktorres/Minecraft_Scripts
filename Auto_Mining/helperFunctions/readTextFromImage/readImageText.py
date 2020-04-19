import cv2
import pytesseract
from helperFunctions.Retrieve_SSIM.screenshot import takeScreenshot
from helperFunctions.Retrieve_SSIM.cropImage import cropImage
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def detectLava(queue, i):
    image = takeScreenshot()
    newImage = cropImage(1445, 360, 500, 320, image)
    newImage.save('./tmp/targetd_fluid%i.png' % i)
    img = cv2.imread('./tmp/targetd_fluid%i.png' % i)
    newString = ""
    try:
        newString = pytesseract.image_to_string(img).split("Targeted Fluid", 1)[1]
    except:
        test = 1
    if 'lava' in newString:
        queue.put(True)
    else:
        queue.put(False)

def detectLavaNoQueue(i):
    image = takeScreenshot()
    newImage = cropImage(1445, 360, 500, 320, image)
    newImage.save('./tmp/targetd_fluid%i.png' % i )
    img = cv2.imread('./tmp/targetd_fluid%i.png' % i)
    newString = ""
    try:
        newString = pytesseract.image_to_string(img).split("Targeted Fluid", 1)[1]
    except:
        test = 1
    if 'lava' in newString:
        return True
    else:
        return False