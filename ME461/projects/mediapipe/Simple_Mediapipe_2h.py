# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:24:26 2023

@author: Yerli Zeka
"""

# Import Libraries
import mediapipe as mp
import cv2
import numpy as np
from Hand_Numbers import *
import copy

## Function Definitions

# Seperate Functions
def condition_rock(ip, it, mp, mt, rp, rt, pp, pt):
    if (ip < it) and (mp < mt) and (rp < rt) and (pp < pt):
        return True
    return False
def condition_paper(ip, it, mp, mt, rp, rt, pp, pt):
    if (ip > it) and (mp > mt) and (rp > rt) and (pp > pt):
        return True
    return False
def condition_scissors(ip, it, mp, mt, rp, rt, pp, pt):
    if (ip > it) and (mp > mt) and (rp < rt) and (pp < pt):
        return True
    return False

# Boxing Function
def GetRect(hand_landmarks, w, h):
    x_max = 0
    y_max = 0
    x_min = w
    y_min = h
    for lm in hand_landmarks.landmark:
        x, y = int(lm.x * w), int(lm.y * h)
        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x
        if y > y_max:
            y_max = y
        if y < y_min:
            y_min = y

    return [x_min, y_min, x_max, y_max]

def Label_Rect(x_start, y_start, state, Player, Win):
    Win = ""
    Rect_txt = state
    cv2.putText(
        frame,
        text = Rect_txt,
        org = (x_start, y_start - 20),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 1.0,
        color = (125, 246, 0),
        thickness = 1
        )

    

# Main Code
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
                    static_image_mode = False,  
                    max_num_hands = 3,
                    min_detection_confidence = 0.5) as hands:
    
    while(cap.isOpened()):
    #while True:
        ret, frame = cap.read()
        h, w, c = frame.shape
              
        if ret == False:
            print("Wow")
            break
        
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        txt = ""
        Win = ""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame,
                                          hand_landmarks,
                                          mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style()
                    )
                # Classification
                hn = hand_landmarks
                ip = hn.landmark[INDEX_FINGER_PIP].y
                it = hn.landmark[INDEX_FINGER_TIP].y
                mp = hn.landmark[MIDDLE_FINGER_PIP].y
                mt = hn.landmark[MIDDLE_FINGER_TIP].y
                rp = hn.landmark[RING_FINGER_PIP].y
                rt = hn.landmark[RING_FINGER_TIP].y
                pp = hn.landmark[PINKY_FINGER_PIP].y
                pt = hn.landmark[PINKY_FINGER_TIP].y
                txt = ""
                
                bc = GetRect(hand_landmarks, w, h)               
                cv2.rectangle(frame, (bc[0], bc[1]), (bc[2], bc[3]), (0, 255, 0), 2)
                
                if(condition_rock(ip, it, mp, mt, rp, rt, pp, pt)):
                    txt = "rock"
                elif(condition_scissors(ip, it, mp, mt, rp, rt, pp, pt)):
                    txt = "scissors"
                elif(condition_paper(ip, it, mp, mt, rp, rt, pp, pt)):
                    txt = "paper"
    
                Label_Rect(bc[0], bc[1], txt, 1, Win)
        
            #cv2.imshow('Rock, Paper, Scissors', frame)
        cv2.imshow('Rock, Paper, Scissors', frame)
        if cv2.waitKey(1) == 27:  
            break

cv2.destroyAllWindows()
cap.release()

