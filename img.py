import cv2
import matplotlib.pyplot as plt

img = plt.imread('./test.jpg')

img = cv2.GaussianBlur(img, (5,5), 0)
img = cv2.resize(img, (244, 128))  # Size changed
img = cv2.Canny(img, 50, 150)

plt.imshow(img)
plt.show()