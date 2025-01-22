import cv2

img = cv2.imread('cat.jpeg')
img_gray = cv2.imread('cat.jpeg', 0)  # Fixed the file name and extension

"""
item: get the pixel value
img.item(y, x, colour)
"""
print('Blue:', img.item(10, 10, 0))  # 10, 10 pixel's blue value
print('Green:', img.item(10, 10, 1))  # 10, 10 pixel's green value
print('Red:', img.item(10, 10, 2))  # 10, 10 pixel's red value

"""
itemset: set the pixel value
img.itemset(y, x, colour, value)
img.itemset((10, 10, 0), 0)  # 10, 10 pixel's blue value to 0

AttributeError: `itemset` was removed from the ndarray class in NumPy 2.0. Use `arr[index] = value` instead.
"""
img[10, 10, 0] = 255

# Set the pixel value of the first 50x50 pixels to 0
# for y in range(50): 
#     for x in range(50):
#         img[y, x, 0] = 0 # it made the pixels color yellow
        

"""
shape: get the image shape
"""
print('Image Shape:', img.shape) # 3 channels, 3 colors
print('Gray Image Shape:', img_gray.shape) # 1 channel, 1 color

y, x, c = img.shape
print('Y:', y, 'X:', x, 'Color:', c)


"""
size: get the image size
"""
print('Image Size:', img.size) # y * x * c
print('Gray Image Size:', img_gray.size) # y * x


"""
datatype: get the image datatype
"""
print('Image Datatype:', img.dtype) # uint8


"""
ROI: Region of Interest
roi = img[y1:y2, x1:x2] 
"""
roi = img[108:147, 67:122] # cat's eye
# cv2.imshow('ROI', roi)

# Copy the cat's eye to the top left corner
# while copying, the size of the roi and the size of the copied area must be the same. If not, it will give an error.
# img[0:39, 0:55] = roi # cat's eye to the top left corner

"""
color filtering: filtering the image by color
"""
# If we make the blue, green and red channels 0, the image will be black.
# img[:, :, 0] = 0 # blue channel to 0
# img[:, :, 1] = 0 # green channel to 0
# img[:, :, 2] = 0 # red channel to 0

# If we make the blue, green and red channels 255, the image will be white.
# img[:, :, 0] = 255 # blue channel to 255
# img[:, :, 1] = 255 # green channel to 255
# img[:, :, 2] = 255 # red channel to 255


cv2.imshow('Image', img)
cv2.waitKey(0) # wait until any key is pressed
cv2.destroyAllWindows()