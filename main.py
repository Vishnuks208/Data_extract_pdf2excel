import cv2
import numpy as np
import pytesseract
import os
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



path = 'C:\\Users\\ksvis\\PycharmProjects\\deb\\pic'
mypiclist = os.listdir(path)
#print(mypiclist)

mydata = {}
for i in mypiclist:

    if i == 'Invoice1.png':

        roi1 = [[(950, 200), (1003, 230),  'Sample of Payment'],
                [(366, 264), (478, 296), 'Payer Mame'],
               [(950, 466), (1058, 496),  'Date'],
               [(1320, 414), (1428, 444),  'Cheque no:'],
               [(1104, 412), (1152, 440),  'Bank code'],
               [(322, 1218), (640, 1280),  'Benefits paid to']]

        #for w in roi1:
        #    print(w[3],',')

        img1 = cv2.imread(i)
        h, w, c = img1.shape

        orb1 = cv2.ORB_create(1000)
        kp1, des1 = orb1.detectAndCompute(img1, None)
        imgkp1 = cv2.drawKeypoints(img1, kp1, None)
        #cv2.imshow(i+' Keypoint',imgkp1)
        #cv2.imshow(i +' Output', img1)

        imgshow1 = img1.copy()
        imgmask1 = np.zeros_like(imgshow1)


        for x,r in enumerate(roi1):

            cv2.rectangle(imgmask1, (r[0][0],r[0][1]),(r[1][0],r[1][1]),(0,255,0),cv2.FILLED)
            imgshow1 = cv2.addWeighted(imgshow1,0.99,imgmask1,0.1,0)

            imgcrop1 = imgshow1[r[0][1]:r[1][1], r[0][0]:r[1][0]]
            cv2.imshow(str(x),imgcrop1)
            #print('{}:{}'.format(r[2], pytesseract.image_to_string(imgcrop1)))
            mydata[r[2]]=(pytesseract.image_to_string(imgcrop1))

        #imgshow1 = cv2.resize(imgshow1, (w // 3, h // 3))
        #cv2.imshow( i, imgshow1)
        #cv2.waitKey(0)


    else:
        roi2 = [[(1279, 427), (1439, 458),  'Provider ID'],
                [(1278, 461), (1409, 490),  'Federal tax ID'],
                [(1277, 492), (1441, 522),  'Remittence ID'],
                [(1283, 525), (1401, 550),  'cheque no'],
                [(1279, 550), (1339, 583),  'Bank Code'],
                [(563, 1448), (636, 1480),  'Charge'],
                [(431, 898), (517, 919),  'Billing NPI Number'],
                [(431, 924), (538, 946),  'Provider Name'],
                [(431, 950), (541, 975),  'Patient Name'],
                [(431, 977), (538, 1000),  'Subscriber Name'],
                [(433, 998), (623, 1022),  'Plan Type'],
                [(687, 1141), (741, 1169), 'Allowed Amount'],
                [(805, 1141), (847, 1167),  'Deductible'],
                [(879, 1139), (956, 1172),  'Copay'],
                [(1016, 1138), (1063, 1167), 'Coinsur'],
                [(1119, 1138), (1167, 1162),  'Provider Discount'],
                [(1221, 1138), (1278, 1167),  'Fee Deduction'],
                [(1439, 1136), (1489, 1165), 'Benefit Amount'],
                [(1450, 1179), (1494, 1209),  'Total Paid'],
                [(959, 1187), (1012, 1209),  'MBR Responsibility']]

        #for o in roi2:
        #    print(o[3],',')

        img2 = cv2.imread(i)
        h, w, c = img2.shape

        orb2 = cv2.ORB_create(1000)
        kp2, des2 = orb2.detectAndCompute(img2, None)
        imgkp2 = cv2.drawKeypoints(img2, kp2, None)
        #cv2.imshow(i + ' Keypoint', imgkp2)
        #cv2.imshow(i + ' Output', img2)
        #cv2.waitKey(0)

        imgshow2 = img2.copy()
        imgmask2 = np.zeros_like(imgshow2)

        for x, r in enumerate(roi2):
            cv2.rectangle(imgmask2, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (0, 255, 0), cv2.FILLED)
            imgshow2 = cv2.addWeighted(imgshow2, 0.99, imgmask2, 0.1, 0)

            imgcrop2 = imgshow2[r[0][1]:r[1][1], r[0][0]:r[1][0]]

            cv2.imshow(str(x),imgcrop2)

            #print('{}:{}'.format(r[2],pytesseract.image_to_string(imgcrop2)))

            mydata[r[2]]=(pytesseract.image_to_string(imgcrop2))

        #imgshow2 = cv2.resize(imgshow2, (w // 3, h // 3))
        #cv2.imshow(i, imgshow2)
        #cv2.waitKey(0)

for key,value in mydata.items():
    print(key,' : ',value)
with open('data.xlsx','a+') as f:
    df = pd.DataFrame(data=mydata, index=[1])
    df.to_excel("data.xlsx", index=False)