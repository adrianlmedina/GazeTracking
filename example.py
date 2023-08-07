"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import pyscreenshot as ImageGrab
from gaze_tracking import GazeTracking
from PIL import Image


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

specific_counter = 0
fullscreen_counter = 0
max_images = 9

locations = [
    (150, 100, 640, 360),
    (640, 100, 1130, 360),
    (1130, 100, 1920, 360),
    (150, 360, 640, 620),
    (640, 360, 1130, 620),
    (1130, 360, 1920, 620),
    (150, 620, 640, 880),
    (640, 620, 1130, 880),
    (1130, 620, 1920, 880),
] 

while True: #img_counter < max_images:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    #text = ""
    # if gaze.is_blinking():
    #     text = "Blinking"
    # elif gaze.is_right():
    #     text = "Looking right"
    # elif gaze.is_left():
    #     text = "Looking left"
    # elif gaze.is_center():
    #     text = "Looking center"

    # cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Camera Feed", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' key to exit the program
        break
    elif key == ord('a') and specific_counter < max_images:
        bbox = locations[specific_counter % len(locations)]
        im = ImageGrab.grab(bbox=bbox)
        im.save(f"filename_specific_{specific_counter + 1}.png")
        print("Screenshot {} taken from specific location!".format(specific_counter + 1))
        specific_counter += 1
        
    elif key == 32 and fullscreen_counter < max_images:
        _, full_frame = webcam.read()  # Capture the entire frame from the webcam
        im = Image.fromarray(cv2.cvtColor(full_frame, cv2.COLOR_BGR2RGB))
        im.save(f"filename_fullscreen_{fullscreen_counter + 1}.png")
        print("Full-screen screenshot {} taken!".format(fullscreen_counter + 1))
        fullscreen_counter += 1

        """im = ImageGrab.grab()
        im.save(f"filename_fullscreen_{fullscreen_counter + 1}.png")
        print("Full-screen screenshot {} taken!".format(fullscreen_counter + 1))
        fullscreen_counter += 1
""" 


    """if cv2.waitKey(1) == 32:
        img_counter += 1
        img_name = "open_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

    elif cv2.waaitKey(1) == 27:
        break
"""
    """if cv2.waitKey(1) == ord('a'):
        im1=ImageGrab.grab(bbox=(150, 100, 640, 360))
        im2=ImageGrab.grab(bbox=(640, 100, 1130, 360))
        im3=ImageGrab.grab(bbox=(1130, 100, 1920, 360))
        im4=ImageGrab.grab(bbox=(150, 360, 640, 620))
        im5=ImageGrab.grab(bbox=(640, 360, 1130, 620))
        im6=ImageGrab.grab(bbox=(1130, 360, 1920, 620))
        im7=ImageGrab.grab(bbox=(150, 620, 640, 880))
        im8=ImageGrab.grab(bbox=(640, 620, 1130, 880))
        im9=ImageGrab.grab(bbox=(1130, 620, 1920, 880))

        im1.save("filename1.png")
        im2.save("filename2.png")
        im3.save("filename3.png")
        im4.save("filename4.png")
        im5.save("filename5.png")
        im6.save("filename6.png")
        im7.save("filename7.png")
        im8.save("filename8.png")
        im9.save("filename9.png")

locations = [
    (150, 100, 640, 360),
    (640, 100, 1130, 360),
    (1130, 100, 1920, 360),
    (150, 360, 640, 620),
    (640, 360, 1130, 620),
    (1130, 360, 1920, 620),
    (150, 620, 640, 880),
    (640, 620, 1130, 880),
    (1130, 620, 1920, 880),
] 
"""
"""screenshot_count = 1
while True:
    if cv2.waitKey(1) == ord('a'):
        if screenshot_count <= len(locations):
            bbox = locations[screenshot_count - 1]
            im = ImageGrab.grab(bbox=bbox)
            im.save(f"filename{screenshot_count}.png")
            print("{} written!".format(screenshot_count))
            screenshot_count += 1
        #elif cv2.waitKey(1) == 27:
        else:
            break
       # break
    #break
"""

webcam.release()
cv2.destroyAllWindows()
 