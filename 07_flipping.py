import argparse
from cv2 import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)
h, w = image.shape[:2]  # i primi due valori della tupla
cv2.imshow("image", image)
cv2.waitKey()

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped horizontally", flipped)
cv2.waitKey()

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped vertically", flipped)
cv2.waitKey()
