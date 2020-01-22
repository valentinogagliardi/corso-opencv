import argparse
from cv2 import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)

print(f"image.shape: {image.shape}")
print(f"image.dtype: {image.dtype}")

"""
nelle matrici numpy:
Y (righe) - X (colonne)
altezza - larghezza
"""
print(f"width: {image.shape[1]}")
print(f"height: {image.shape[0]}")

cv2.imshow("image", image)
cv2.waitKey()

cv2.imwrite(filename="out/01_image.jpg", img=image)
