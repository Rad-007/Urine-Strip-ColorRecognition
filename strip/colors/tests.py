from django.test import TestCase

# Create your tests here.
import cv2
image = cv2.imread('sample/image1.jpg')

clone = image.copy()
boxes = []

def mouse_callback(event, x, y, flags, param):
    global boxes

    if event == cv2.EVENT_LBUTTONDOWN:
        boxes.append((x, y))
        cv2.rectangle(clone, boxes[-1], (x, y), (0, 255, 0), 2)
        cv2.imshow('Urine Strip', clone)

cv2.namedWindow('Urine Strip')
cv2.setMouseCallback('Urine Strip', mouse_callback)

while True:
    cv2.imshow('Urine Strip', clone)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        clone = image.copy()
        boxes = []
    elif key == ord('q') or len(boxes) >= 10:
        break

cv2.destroyAllWindows()

for i, box in enumerate(boxes):
    print(f'Box {i+1}: {box}')