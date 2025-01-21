import cv2

cap = cv2.VideoCapture('cat.mp4')

if cap.isOpened() == False:
    print('Error opening video file')

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True: # if frame is read correctly
        cv2.imshow('frame', frame)
        
        kInp = cv2.waitKey(24) # 24 means 24ms time
        if kInp == ord('q'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()