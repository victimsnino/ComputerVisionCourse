import numpy as np
import cv2 as cv

img = cv.imread('GOPR01170000.jpg')

conf = cv.FileStorage('camera.xml', cv.FILE_STORAGE_READ)

camera_matrix= conf.getNode('camera_matrix').mat()
dist_coefs = conf.getNode('distortion_coefficients').mat()

h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

dst = cv.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

cv.imwrite('GOPR01170000_undistort.jpg', dst)