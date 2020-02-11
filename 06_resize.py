import argparse
from cv2 import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)
h, w = image.shape[:2]

cv2.imshow("image", image)
cv2.waitKey()

# resize by width
new_width = 300
resize_ratio = new_width / w
dim = (new_width, int(h * resize_ratio))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("image resized", resized)
cv2.waitKey()

# resize by height
new_height = 300
resize_ratio = new_height / h
dim = (int(w * resize_ratio), new_height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("image resized", resized)
cv2.waitKey()

# resize by percent
resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("image resized", resized)
cv2.waitKey()
