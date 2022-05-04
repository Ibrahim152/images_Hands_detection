import mediapipe as mp
import cv2
import numpy as np
import uuid
import os


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
try:
    os.mkdir('output Image')
except:
    pass
cap = cv2.imread('test.jpg')

with mp_hands.Hands(min_detection_confidence=0, min_tracking_confidence=0.5) as hands:
    frame = cap
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    print(results)

    if results.multi_hand_landmarks:
        for num, hand in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4), mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),)
        cv2.imwrite(os.path.join('output Image',
                    '{}.jpg'.format(uuid.uuid1())), image)
        cv2.imshow('Hand Tracker', image)
# cap.release()
# cv2.destroyAllWindows()
# mp_drawing.DrawingSpec()
