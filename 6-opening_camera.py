import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    
    cv2.imshow('frame', frame)
    
    cv2.waitKey(0)
    
    kInp = cv2.waitKey(0) # 0 means infinite time
    kInp = cv2.waitKey(1) # 1 means 1ms time
    kInp = cv2.waitKey(1000) # 1000 means 1s time
    
    if kInp == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
