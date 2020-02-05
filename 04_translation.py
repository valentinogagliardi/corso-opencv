import argparse
import numpy as np
from cv2 import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)
h, w = image.shape[:2]
cv2.imshow("image", image)
cv2.waitKey()

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("shifted", shifted)
cv2.waitKey()

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("shifted", shifted)
cv2.waitKey()


def translate(image, x, y):
    h, w = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (w, h))


shifted = translate(image, x=0, y=100)
cv2.imshow("shift func", shifted)
cv2.waitKey()
