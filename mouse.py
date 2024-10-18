import cv2 as cv
import mediapipe as mp
import pyautogui
capture = cv.VideoCapture(0)
detect = mp.solutions.hands.Hands()
mp_draw = mp.solutions.drawing_utils
width, height = pyautogui.size()
l_x = 0
in_x = 0
while True:
    running, frame = capture.read()
    frame_height, frame_width, running = frame.shape
    frame = cv.flip(frame, 1)
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    output = detect.process(rgb)
    hands = output.multi_hand_landmarks
    if hands:
        for hand_landmarks in hands:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            for id, mark in enumerate(landmarks):
                x = int(mark.x * frame_width)
                y = int(mark.y * frame_height)
                if id == 12:
                    in_x = (width / frame_width) * x
                    in_y = (height / frame_height) * y
                    cv.circle(img=frame, center=(x,y), radius=10, color=(70, 223, 255))
                    pyautogui.moveTo(in_x, in_y)
                
                if id == 8:
                    cv.circle(img=frame, center=(x,y), radius=10, color=(70, 23, 255))
                    t_x = (width / frame_width) * x
                    t_y = (height / frame_height) * y
                    
                    if abs(in_x - t_x) < 30:
                        pyautogui.click()
                       
    cv.imshow("track", frame)
    cv.waitKey(1)