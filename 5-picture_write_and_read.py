import cv2

# Read an image
img = cv2.imread('cat.jpeg') # read the image
img = cv2.imread('cat.jpeg', cv2.IMREAD_GRAYSCALE) # read the image in grayscale
img = cv2.imread('cat.jpeg', 0) # read the image in grayscale
img = cv2.imread('cat.jpeg', 1) # read the image in color

cv2.imshow('cat image', img)


# cv2.waitKey(0) # 0 means wait for any key press

kInp = cv2.waitKey(0) # 0 means wait for any key press
print(kInp) # print the key pressed

if kInp == 27: # 27 is the ASCII value of the escape key
    print('Escape key is pressed')
    cv2.destroyAllWindows() # close the window
elif kInp == ord('a'):
    print('a key is pressed')
else:
    print('Any key is pressed')

cv2.destroyAllWindows() # close the window

##############################################

img2 = cv2.imread('cat.jpeg', 0) # read the image
cv2.imwrite('cat2.jpeg', img2) # write the image