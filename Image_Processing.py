import cv2
import numpy as np

img = cv2.imread("No1Frame235.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (480, 270))
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
hls_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
hls_image_sharp = cv2.filter2D(src=hls_gray, ddepth=-1, kernel=kernel)

cv2.imshow("RGB to HLS", img)
cv2.imshow("HLS to GRAY and sharped Image", hls_image_sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()

