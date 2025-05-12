import cv2
import numpy as np

image = np.ones((500, 500, 3), dtype=np.uint8) * 255
center = (250, 250)
green = (0, 180, 0)
dark_green = (0, 100, 0)
radius = 40
offset = 60
positions = [
    (center[0], center[1] - offset),
    (center[0] + offset, center[1]),
    (center[0], center[1] + offset),
    (center[0] - offset, center[1])
]

cv2.namedWindow('Clover', cv2.WINDOW_AUTOSIZE)

for pos in positions:
    for r in range(1, radius + 1, 2):
        temp = image.copy()
        cv2.circle(temp, pos, r, green, 2)
        cv2.imshow('Clover', temp)
        cv2.waitKey(15)
    cv2.circle(image, pos, radius, green, -1)
    cv2.imshow('Clover', image)
    cv2.waitKey(100)

for r in range(0, 21, 2):
    temp = image.copy()
    cv2.circle(temp, center, r, dark_green, -1)
    cv2.imshow('Clover', temp)
    cv2.waitKey(20)
image = temp

for y in range(270, 400, 5):
    temp = image.copy()
    cv2.line(temp, (250, 270), (250, y), dark_green, thickness=10)
    cv2.imshow('Clover', temp)
    cv2.waitKey(15)
image = temp

cv2.waitKey(0)
cv2.destroyAllWindows()
