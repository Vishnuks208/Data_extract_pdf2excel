import cv2
import random

scale = 0.55
circles = []
counter = 0
counter2 = 0
point1 = []
point2 = []
mypoints = []
mycolor = []

def mousepoints(event,x,y,flags,params):
    global counter,point1,point2,counter2,circles,mycolor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter == 0:
            point1 = int(x//scale), int(y//scale);
            counter += 1
            mycolor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200)
        elif counter == 1:
            point2 = int(x//scale), int(y//scale)
            type = input('Enter Type : ')
            name = input('Enter Name : ')
            mypoints.append([point1,point2,type,name])
            counter = 0
        circles.append([x,y,mycolor])
        counter2 += 1
#img = cv2.imread('Invoice1.png')
img = cv2.imread('Invoice2.png')
#h, w, c = img.shape
#img = cv2.resize(img, (w // 2, h // 2))
img = cv2.resize(img, (0, 0), None, scale, scale)


while True:
    for x,y,color in circles:
        cv2.circle(img, (x,y),3 , color, cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousepoints)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(mypoints)
        break

