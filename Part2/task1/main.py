import cv2
import numpy as np

# Open
orig_img = cv2.imread('whiteballssample.jpg')

img  = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
# Binarize
_, img = cv2.threshold(img,115,255, cv2.THRESH_BINARY)

# Remove noise and try to make balls differs
kernel = np.ones((3,3),np.uint8)

kernel[0, 2] = 0
kernel[2, 0] = 0
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=20)

# Find contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(orig_img, contours, -1, (0,0,255), 3)

print(f'Find {len(contours)} different balls')

# Find suitable by size circles
circles = [cv2.minEnclosingCircle(contour) for contour in contours]
radiuses = []
for center, radius in circles:
    img = cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0,255,0), 5)
    radiuses.append(radius)

mean_radius = np.mean(radiuses)
variance = np.var(radiuses)

print(f'Mean radius {mean_radius}')
print(f'Var radius {variance}')

(w, h) = img.shape[:2]
coefficient_to_out = 2/3
# cv2.imwrite('balls_with_circles.jpg', img)
cv2.imshow("result", cv2.resize(img, (int(h*coefficient_to_out), int(w*coefficient_to_out))))
cv2.waitKey(0)