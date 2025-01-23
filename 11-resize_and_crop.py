import cv2

"""
Resize Image
"""
img = cv2.imread('cat.jpeg')
print('Original Size ->', img.shape) # Original Size -> (225, 194, 3)

imgResized = cv2.resize(img, (150, 250)) # (Width, Height)  = x, y
print('Resized Size ->', imgResized.shape) # Resized Size -> (250, 150, 3) = (Height, Width, Channel)
cv2.imshow('Resized Image', imgResized)
""""""
y, x, c = img.shape
imgResized2 = cv2.resize(img, (x+x//2, y+y//2)) 
print('Resized 2 Size ->', imgResized2.shape) # Resized 2 Size -> (337, 291, 3)
cv2.imshow('Resized Image 2', imgResized2)

""" 
Crop Image
"""
imgCropped = img[0:200, 0:150] # [y1:y2, x1:x2]
cv2.imshow('Cropped Image', imgCropped)
""""""
y, x, c = img.shape
imgCropped2 = img[0:y//2, 0:x//2] # [y1:y2, x1:x2] -> left top
cv2.imshow('Cropped Image 2', imgCropped2)

imgCropped3 = img[0:y//2, x//2:x] # [y1:y2, x1:x2] -> right top
cv2.imshow('Cropped Image 3', imgCropped3)

imgCropped4 = img[y//2:y, 0:x//2] # [y1:y2, x1:x2] -> left bottom
cv2.imshow('Cropped Image 4', imgCropped4)

imgCropped5 = img[y//2:y, x//2:x] # [y1:y2, x1:x2] -> right bottoms
cv2.imshow('Cropped Image 5', imgCropped5)


cv2.imshow('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()