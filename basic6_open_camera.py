import cv2

cap = cv2.VideoCapture(0) 

while (True): #ตรวจสอบ
    check , fraem = cap.read() 
    cv2.imshow("Output",fraem) 

    if cv2.waitKey(1) & 0xFF == ord("e"): 
        break 

cap.release() 
cv2.destroyAllWindows()

