import cv2

vid = cv2.VideoCapture(0) # vid is the object of the camera

w = int(vid.get(3)) # 3 is the width of the frame
h = int(vid.get(4)) # 4 is the height of the frame

size = (w, h) # size of the frame

result = cv2.VideoWriter('record.mp4', cv2.VideoWriter_fourcc(*'XVID'), 24, size) # result is the object of the video file

# fourcc is a 4-byte code used to specify the video codec -> https://www.fourcc.org/downloads/

while True:
    ret, frame = vid.read()
    
    if ret == True:
        result.write(frame)
        
        cv2.imshow('frame', frame)
        
        kInp = cv2.waitKey(24)
        if kInp == ord('s'):
            break
    
    else:
        break
    
vid.release() # release the camera
result.release() # release the video file
cv2.destroyAllWindows() # destroy all the windows

print('Video saved successfully!')