import cv2

"""
Normal Addition of two images
"""
img1 = cv2.imread('cat.jpeg')
# img2 = cv2.imread('opencv_logo.png')
print('Image 1 shape:', img1.shape) # (194, 259, 3)
# print('Image 2 shape:', img2.shape) # (194, 260, 3)

# totalImg = cv2.add(img1, img2) # Add the pixel values of the two images
# # it  gives error because both images are of different sizes

img3 = cv2.imread('cat2.jpeg')
print('Image 3 shape:', img3.shape) # (194, 259, 3)

totalImg = cv2.add(img1, img3) # Add the pixel values of the two images
# it doesn't give error because both images are of same sizes

print('img1', img1[160, 80]) # [40 63 85]
print('img3', img3[160, 80]) # [67 67 67]
print('totalImg', totalImg[160, 80]) # [107 130 152]

cv2.imshow('Image 1', img1)
cv2.imshow('Image 3', img3)
cv2.imshow('Total Image', totalImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Weighted Addition of two images
"""
totalWeightedImg = cv2.addWeighted(img1, 0.7, img3, 0.3, 0) # (img1, weight1, img2, weight2, gamma)

print('img1', img1[160, 80]) # [40 63 85]
print('img3', img3[160, 80]) # [67 67 67]
print('totalWeightedImg', totalWeightedImg[160, 80]) # [48 64 80]

cv2.imshow('Total Weighted Image', totalWeightedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Difference of two methods:
    cv2.add() - Adds two images
    cv2.addWeighted() - Adds two images with different weights

"""