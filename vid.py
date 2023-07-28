import cv2
import numpy as np

from gaze_tracking import GazeTracking
cap = cv2.VideoCapture(0)  

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()
    #bgr_frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    out.write(frame)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

