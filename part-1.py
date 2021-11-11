import cv2
# load image
img = cv2.imread('assets/image1cv.jpg', 1)
# resize image
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3 )
# image rotate 
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindow()
