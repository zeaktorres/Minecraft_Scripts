
import pyscreenshot as ImageGrab
import tempfile
import os
from PIL import Image 
import time
import shutil

def takeScreenshot():
    # grab fullscreen
    im = ImageGrab.grab()
    # save image file
    try:
        os.mkdir("./tmp")
    except OSError as e:
        test = 1
    return im