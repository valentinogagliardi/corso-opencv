import argparse
from cv2 import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)

# ricava la dimensione dell'immagine
h, w = image.shape[:2]
center = (w // 2, h // 2)
cv2.imshow("image", image)
cv2.waitKey()

# matrice di rotazione
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# trasformazione affine
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated by 45°", rotated)
cv2.waitKey()

# trasformazione affine
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated by 90°", rotated)
cv2.waitKey()


def rotateBy(image, angle, center=None, scale=1.0):
    h, w = image.shape[:2]
    if not center:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))


cv2.imshow("rotated by 180°", rotateBy(image, 180))
cv2.waitKey()

# la rotazione cv2 built-in è limitata a 90 e 180
rotated = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("built-in func", rotated)
cv2.waitKey()
