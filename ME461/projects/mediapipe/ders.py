import mediapipe as mp
import cv2
import numpy as np
import statistics as st
import time
capture = cv2.VideoCapture(0)

def calc_dist(origin_landmark, landmark):
	dist = np.sqrt((origin_landmark.x - landmark.x)**2 + (origin_landmark.y - landmark.y)**2)
	return dist
finger_indecies=[6,8,10,12,14,16,18,20]

def condition(hand_landmarks):
	fingerdistances = {'indexf': [calc_dist(hand_landmarks[0], hand_landmarks[8]), calc_dist(hand_landmarks[0], hand_landmarks[6])]
					,'middlef': [calc_dist(hand_landmarks[0], hand_landmarks[12]), calc_dist(hand_landmarks[0], hand_landmarks[10])]
					,'ringf': [calc_dist(hand_landmarks[0], hand_landmarks[16]), calc_dist(hand_landmarks[0], hand_landmarks[14])]
					,'pinkyf': [calc_dist(hand_landmarks[0], hand_landmarks[20]), calc_dist(hand_landmarks[0], hand_landmarks[18])]}
	if fingerdistances['indexf'][0]>fingerdistances['indexf'][1] and fingerdistances['middlef'][0]>fingerdistances['middlef'][1] and fingerdistances['ringf'][0]>fingerdistances['ringf'][1] and fingerdistances['pinkyf'][0]>fingerdistances['pinkyf'][1]:
		return 'PAPER!'
	elif fingerdistances['indexf'][0]<fingerdistances['indexf'][1] and fingerdistances['middlef'][0]<fingerdistances['middlef'][1] and fingerdistances['ringf'][0]<fingerdistances['ringf'][1] and fingerdistances['pinkyf'][0]<fingerdistances['pinkyf'][1]:
		return 'ROCK!'
	elif fingerdistances['indexf'][0]>fingerdistances['indexf'][1] and fingerdistances['middlef'][0]>fingerdistances['middlef'][1] and fingerdistances['ringf'][0]<fingerdistances['ringf'][1] and fingerdistances['pinkyf'][0]<fingerdistances['pinkyf'][1]:
		return 'SCISSORS!'
	else:
		return 'none'

drawing = mp.solutions.drawing_utils
drawingstyles = mp.solutions.drawing_styles
hands = mp.solutions.hands.Hands(static_image_mode = False, min_detection_confidence = 0.7)
keyboard = 31
gamestate1 = 1
while True : 
	deneme = 0
	while gamestate1:
		data, image = capture.read()
		image = cv2.flip(image, 1)
		

		if keyboard == 32:
			deneme=1
			starttime = time.time()
		
		if deneme:
			if (time.time() - starttime) < 1:
				cv2.putText(img = image, text = "STARTS IN 3...", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
			elif (time.time() - starttime) < 2:
				cv2.putText(img = image, text = "STARTS IN 2...", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
			elif (time.time() - starttime) < 3:
				cv2.putText(img = image, text = "STARTS IN 1...", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
			elif (time.time() - starttime) < 4:
				gamestate2 = 1
				gamestate1  = 0
		cv2.imshow("GRUP YERLI-ZEKA", image)
		keyboard = cv2.waitKey(1) 

	while gamestate2:
		p1 = 0
		p2 = 1
		data, image = capture.read()
		image = cv2.flip(image, 1)
		image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		results = hands.process(image2)
		if results.multi_hand_landmarks:
			if len(results.multi_hand_landmarks) ==0:
				pass
			if len(results.multi_hand_landmarks) >=1:
				wristp1 = results.multi_hand_landmarks[p1].landmark[0]
				thumb1p1 = results.multi_hand_landmarks[p1].landmark[1]
				thumb2p1 = results.multi_hand_landmarks[p1].landmark[2]
				thumb3p1 = results.multi_hand_landmarks[p1].landmark[3]
				thumb4p1 = results.multi_hand_landmarks[p1].landmark[4]
				index1p1 = results.multi_hand_landmarks[p1].landmark[5]
				index2p1 = results.multi_hand_landmarks[p1].landmark[6]
				index3p1 = results.multi_hand_landmarks[p1].landmark[7]
				index4p1 = results.multi_hand_landmarks[p1].landmark[8]
				middle1p1 = results.multi_hand_landmarks[p1].landmark[9]
				middle2p1 = results.multi_hand_landmarks[p1].landmark[10]
				middle3p1 = results.multi_hand_landmarks[p1].landmark[11]
				middle4p1 = results.multi_hand_landmarks[p1].landmark[12]
				ring1p1 = results.multi_hand_landmarks[p1].landmark[13]
				ring2p1 = results.multi_hand_landmarks[p1].landmark[14]
				ring3p1 = results.multi_hand_landmarks[p1].landmark[15]
				ring4p1 = results.multi_hand_landmarks[p1].landmark[16]
				pinky1p1 = results.multi_hand_landmarks[p1].landmark[17]
				pinky2p1 = results.multi_hand_landmarks[p1].landmark[18]
				pinky3p1 = results.multi_hand_landmarks[p1].landmark[19]
				pinky4p1 = results.multi_hand_landmarks[p1].landmark[20]
			if len(results.multi_hand_landmarks) >=2:
				wristp2 = results.multi_hand_landmarks[p2].landmark[0]
				thumb1p2 = results.multi_hand_landmarks[p2].landmark[1]
				thumb2p2 = results.multi_hand_landmarks[p2].landmark[2]
				thumb3p2 = results.multi_hand_landmarks[p2].landmark[3]
				thumb4p2 = results.multi_hand_landmarks[p2].landmark[4]
				index1p2 = results.multi_hand_landmarks[p2].landmark[5]
				index2p2 = results.multi_hand_landmarks[p2].landmark[6]
				index3p2 = results.multi_hand_landmarks[p2].landmark[7]
				index4p2 = results.multi_hand_landmarks[p2].landmark[8]
				middle1p2 = results.multi_hand_landmarks[p2].landmark[9]
				middle2p2 = results.multi_hand_landmarks[p2].landmark[10]
				middle3p2 = results.multi_hand_landmarks[p2].landmark[11]
				middle4p2 = results.multi_hand_landmarks[p2].landmark[12]
				ring1p2 = results.multi_hand_landmarks[p2].landmark[13]
				ring2p2 = results.multi_hand_landmarks[p2].landmark[14]
				ring3p2 = results.multi_hand_landmarks[p2].landmark[15]
				ring4p2 = results.multi_hand_landmarks[p2].landmark[16]
				pinky1p2 = results.multi_hand_landmarks[p2].landmark[17]
				pinky2p2 = results.multi_hand_landmarks[p2].landmark[18]
				pinky3p2 = results.multi_hand_landmarks[p2].landmark[19]
				pinky4p2 = results.multi_hand_landmarks[p2].landmark[20]
				#player 1 is green
				# if (st.mean([wristp1.x,thumb1p1.x,index1p1.x,ring1p1.x,pinky1p1.x]))<=0.5:
				# 	hand0 = "onleft"
				# 	p1 = 0
				# 	p2 = 1
				# else : 
				# 	p1 = 1
				# 	p2 = 0
			# for j in range(0,21):
			# 	if len(results.multi_hand_landmarks) ==0:
			# 		pass
			# 	if len(results.multi_hand_landmarks) >=1:
			# 		print("X-coord of Hand1:")
			# 		print(results.multi_hand_landmarks[p1].landmark[j].x)
			# 		print("Y-coord of Hand1:")
			# 		print(results.multi_hand_landmarks[p1].landmark[j].y)
			# 	if len(results.multi_hand_landmarks) >=2:
			# 		print("X-coord of Hand2:")
			# 		print(results.multi_hand_landmarks[p2].landmark[j].x)
			# 		print("Y-coord of Hand2:")
			# 		print(results.multi_hand_landmarks[p2].landmark[j].y)

			if len(results.multi_hand_landmarks) ==0:
				pass
			if len(results.multi_hand_landmarks) ==1:
				cv2.putText(img = image, text = condition(results.multi_hand_landmarks[0].landmark), org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,255,255), thickness = 3)
				# cond_paperp1 = (pinky1p1.y > pinky2p1.y and pinky2p1.y > pinky3p1.y and pinky3p1.y > pinky4p1.y and ring1p1.y > ring2p1.y and ring2 p1.y > ring3p1.y and ring3p1.y > ring4p1.y)
				# cond_scissorsp1 = (pinky4p1.y > st.mean([index1p1.y,middle1p1.y]) and ring4p1.y > st.mean([index1p1.y,middle1p1.y]))
				# cond_rockp1 = (index1p1.y < index4p1.y and middle1p1.y < middle4p1.y and ring1p1.y < ring4p1.y and pinky1p1.y < pinky4p1.y)

				# if(cond_paperp1 and not cond_scissorsp1 and not cond_rockp1):
				# 	p1status = "paper"
				# 	cv2.putText(img = image, text = "PAPER!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,255,255), thickness = 3)
				# if(cond_scissorsp1 and not cond_rockp1 and not cond_paperp1):
				# 	p1status = "scissors"
				# 	cv2.putText(img = image, text = "SCISSORS!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,255,255), thickness = 3)
				# if(cond_rockp1 and not cond_paperp1):
				# 	p1status = "rock"
				# 	cv2.putText(img = image, text = "ROCK!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,255,255), thickness = 3)
		
			if len(results.multi_hand_landmarks) >=2:	
				p1status = condition(results.multi_hand_landmarks[p1].landmark)
				cv2.putText(img = image, text = p1status, org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,255,0), thickness = 3)
				# cond_paperp1 = (pinky1p1.y > pinky2p1.y and pinky2p1.y > pinky3p1.y and pinky3p1.y > pinky4p1.y and ring1p1.y > ring2p1.y and ring2p1.y > ring3p1.y and ring3p1.y > ring4p1.y)
				# cond_scissorsp1 = (pinky4p1.y > st.mean([index1p1.y,middle1p1.y]) and ring4p1.y > st.mean([index1p1.y,middle1p1.y]))
				# cond_rockp1 = (index1p1.y < index4p1.y and middle1p1.y < middle4p1.y and ring1p1.y < ring4p1.y and pinky1p1.y < pinky4p1.y)

				# if(cond_paperp1 and not cond_scissorsp1 and not cond_rockp1):
				# 	p1status = "paper"
				# 	cv2.putText(img = image, text = "PAPER!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,255,0), thickness = 3)
				# if(cond_scissorsp1 and not cond_rockp1 and not cond_paperp1):
				# 	p1status = "scissors"
				# 	cv2.putText(img = image, text = "SCISSORS!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,255,0), thickness = 3)
				# if(cond_rockp1 and not cond_paperp1):
				# 	p1status = "rock"
				# 	cv2.putText(img = image, text = "ROCK!", org = (50,50), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,255,0), thickness = 3)
				p2status = condition(results.multi_hand_landmarks[p2].landmark)
				cv2.putText(img = image, text = p2status, org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
				# cond_paperp2 = (pinky1p2.y > pinky2p2.y and pinky2p2.y > pinky3p2.y and pinky3p2.y > pinky4p2.y and ring1p2.y > ring2p2.y and ring2p2.y > ring3p2.y and ring3p2.y > ring4p2.y)
				# cond_scissorsp2 = (pinky4p2.y > st.mean([index1p2.y,middle1p2.y]) and ring4p2.y > st.mean([index1p2.y,middle1p2.y]))
				# cond_rockp2 = (index1p2.y < index4p2.y and middle1p2.y < middle4p2.y and ring1p2.y < ring4p2.y and pinky1p2.y < pinky4p2.y)

				# if(cond_paperp2 and not cond_scissorsp2 and not cond_rockp2):
				# 	p2status = "paper"
				# 	cv2.putText(img = image, text = "PAPER!", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
				# if(cond_scissorsp2 and not cond_rockp2 and not cond_paperp2):
				# 	p2status = "scissors"
				# 	cv2.putText(img = image, text = "SCISSORS!", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
				# if(cond_rockp2 and not cond_paperp2):
				# 	p2status = "rock"
				# 	cv2.putText(img = image, text = "ROCK!", org = (50,150), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (0,0,255), thickness = 3)
				
				if (p1status == p2status):
					cv2.putText(img = image, text = "TIE!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "PAPER!" and p2status == "ROCK!"):
					cv2.putText(img = image, text = "GREEN  WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "PAPER!" and p2status == "SCISSORS!"):
					cv2.putText(img = image, text = "RED  WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "ROCK!" and p2status == "PAPER!"):
					cv2.putText(img = image, text = "RED WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "ROCK!" and p2status == "SCISSORS!"):
					cv2.putText(img = image, text = "GREEN  WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "SCISSORS!" and p2status == "ROCK!"):
					cv2.putText(img = image, text = "RED WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)
				if (p1status == "SCISSORS!" and p2status == "PAPER!"):
					cv2.putText(img = image, text = "GREEN  WINS!", org = (50,100), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 2.0, color = (255,0,0), thickness = 3)


						

			# print("Z-coord:")
			# print(i.landmark[0].z)
			if len(results.multi_hand_landmarks) ==0:
				pass

			# if (hand0 == "onleft"):
			if len(results.multi_hand_landmarks) >=1:
				drawing.draw_landmarks(image, results.multi_hand_landmarks[p1], mp.solutions.hands.HAND_CONNECTIONS, landmark_drawing_spec=drawing.DrawingSpec(color=(0,255,0),circle_radius=3))
			if len(results.multi_hand_landmarks) >=2:
				drawing.draw_landmarks(image, results.multi_hand_landmarks[p2], mp.solutions.hands.HAND_CONNECTIONS, landmark_drawing_spec=drawing.DrawingSpec(color=(0,0,255),circle_radius=3))
			# else :
			# 	if len(results.multi_hand_landmarks) >=1:
			# 		drawing.draw_landmarks(image, results.multi_hand_landmarks[p1], mp.solutions.hands.HAND_CONNECTIONS, landmark_drawing_spec=drawing.DrawingSpec(color=(0,0,255),circle_radius=3))
			# 	if len(results.multi_hand_landmarks) >=2:
			# 		drawing.draw_landmarks(image, results.multi_hand_landmarks[p2], mp.solutions.hands.HAND_CONNECTIONS, landmark_drawing_spec=drawing.DrawingSpec(color=(0,255,0),circle_radius=3))
			
		cv2.imshow("GRUP YERLI-ZEKA", image)
		keyboard = cv2.waitKey(1) 
		if keyboard == 27:
			capture.release()
			cv2.destroyAllWindows()
			break
		if keyboard == 32:
			gamestate2 = 0
			gamestate1  = 1