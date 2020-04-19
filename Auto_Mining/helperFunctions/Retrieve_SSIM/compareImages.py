import cv2
from skimage.metrics import structural_similarity as ssim
def compareImages(queue):
    image1 = cv2.imread('./tmp/image0.png')
    image2 = cv2.imread('./tmp/image1.png')
    image1 = cv2.resize(image1, (100, 100))
    image2 = cv2.resize(image2, (100, 100))
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    s = ssim(image1, image2)
    queue.put(s)