import cv2
import numpy as np

def Game_arena():
    import cv2
    import numpy as np

    #define a function to insert a rectangle with angular orientation into an image
    def draw_rect(img, startx, starty, l, w, theta, color):
        #create mask of size img
        mask = np.zeros(img.shape, dtype=np.uint8)
        #draw the rectangle
        cv2.rectangle(mask, (startx, starty), (startx+l, starty+w), (255,255,255), -1)
        #rotate the image
        M = cv2.getRotationMatrix2D((startx+l/2, starty+w/2), theta, 1)
        rotated = cv2.warpAffine(mask, M, (mask.shape[1], mask.shape[0]))
        #add the rectangle over image
        img = cv2.subtract(img, rotated)
        #Change black to color
        img[np.where((img==[0,0,0]).all(axis=2))] = color
        return img


    #create a white image
    img = np.zeros((500,900,3), np.uint8)
    img.fill(255)
    #border around image
    cv2.rectangle(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 15)
    #Create Rectangles
    img=draw_rect(img, 200, 250, 150, 30, 60, (255,0,0))
    img=draw_rect(img, 550, 250, 150, 30, -60, (255,0,0))
    #draw thick circle
    cv2.circle(img, (450, 250), 25, (0,0,255), 7)
    return img


