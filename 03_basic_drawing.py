import numpy as np
from cv2 import cv2
from src.colors import Colors

image = np.zeros((300, 300, 3), dtype="uint8")

# points (x, y)
p1 = (0, 0)
p2 = (299, 299)

cv2.line(image, p1, p2, color=Colors.GREEN, thickness=1, lineType=cv2.LINE_AA)
cv2.imshow("image", image)
cv2.waitKey()

# points (x, y)
p1 = (299, 0)
p2 = (0, 299)

cv2.line(image, p1, p2, color=Colors.RED)
cv2.imshow("image", image)
cv2.waitKey()

# points (x, y)
p1 = (10, 10)
p2 = (60, 60)
cv2.rectangle(image, p1, p2, color=Colors.DEEPPINK, thickness=1, lineType=cv2.LINE_AA)
cv2.imshow("image", image)
cv2.waitKey()

p1 = (239, 239)
p2 = (289, 289)
cv2.rectangle(image, p1, p2, color=Colors.DEEPPINK, thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow("image", image)
cv2.waitKey()


# Circles
image1 = np.zeros((300, 300, 3), dtype="uint8")
h, w = image.shape[:2]
(center_x, center_y) = (w // 2, h // 2)

for r in range(0, 150, 10):
    cv2.circle(
        image1,
        (center_x, center_y),
        r,
        color=Colors.YELLOW,
        thickness=1,
        lineType=cv2.LINE_AA,
    )
cv2.imshow("circle", image1)
cv2.waitKey()

# Circles 2
image1 = np.zeros((300, 300, 3), dtype="uint8")
h, w = image.shape[:2]
(center_x, center_y) = (w // 2, h // 2)

color = Colors.RED
for r in range(150, 0, -10):
    cv2.circle(
        image1, (center_x, center_y), r, color, thickness=-1, lineType=cv2.LINE_AA,
    )
    color = Colors.GREEN if color == Colors.RED else Colors.RED

cv2.imshow("circle", image1)
cv2.waitKey()
