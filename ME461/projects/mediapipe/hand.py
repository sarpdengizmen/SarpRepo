import mediapipe as mp
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands
hands_mesh=hands.Hands(max_num_hands=1, 
                    static_image_mode=True,
                    min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils


while True:
    _, frm = cap.read()
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)

    result = hands_mesh.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            draw.draw_landmarks(frm, hand_landmarks, hands.HAND_CONNECTIONS)
            print(hand_landmarks)
    cv2.imshow('window', frm)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break


