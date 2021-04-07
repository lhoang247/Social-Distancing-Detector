import cv2
import numpy as np
import matplotlib.pyplot as plt
from CameraMatrix import returnCameraParameters

def SDCalibratedCameraWithNoZ(img,blackBox,filterPeople,stablizer,sBool):
    rm, tm, cm, _ = returnCameraParameters(3)
    rm = np.transpose(rm)
    rtm = np.concatenate((np.reshape(rm[0],(3,1)),np.reshape(rm[1],(3,1))),axis=1)
    rtm = np.concatenate((rtm,np.transpose(tm)),axis=1)
    homography = np.matmul(cm,rtm)

    xCoo = []
    yCoo = []
    notSD = []
    for i in range(len(filterPeople)):

        u = int(filterPeople[i][0] + filterPeople[i][2]/2)
        v = int(filterPeople[i][1] + filterPeople[i][3]*99)
        imagePoint = np.array(([[u],[v],[1]]))
        realWorldCoordinates = np.matmul(np.linalg.inv(homography),imagePoint)
        realWorldCoordinates = realWorldCoordinates / realWorldCoordinates[2]
        xCoo.append(int(realWorldCoordinates[0]))
        yCoo.append(int(realWorldCoordinates[1]))

    for x in range(len(filterPeople)):
        cv2.rectangle(img, (filterPeople[x][0],filterPeople[x][1]), (filterPeople[x][0]+filterPeople[x][2], filterPeople[x][1]+filterPeople[x][3]), (255,255,0), 2)
        for y in range(len(filterPeople)):
            if (x != y):
                distance = np.sqrt(abs(xCoo[x]-xCoo[y])**2 + abs(yCoo[x]-yCoo[y])**2)
                if (distance < 4):
                    cv2.line(img, (int(filterPeople[x][0]+(filterPeople[x][2]*0.5)), int(filterPeople[x][1]+filterPeople[x][3]*0.99)), (int(filterPeople[y][0]+(filterPeople[y][2]*0.5)), int(filterPeople[y][1]+filterPeople[y][3]*0.99)), (0, 0, 255), thickness= 2)
                    notSD.append([x,y])

    xCoo = np.array(xCoo)
    yCoo = np.array(yCoo)
    lowX = np.min(xCoo)
    lowY = np.min(yCoo)
    highX = np.max(xCoo)
    highY = np.max(yCoo)

    if (sBool == False):
        stablizer.append(lowX)
        stablizer.append(lowY)
        stablizer.append(highX)
        stablizer.append(highY)
        sBool = True
        stablizer = np.array(stablizer)

    xCoo = abs((xCoo - stablizer[0]) / (stablizer[2] - stablizer[0])-1) 
    yCoo = abs((yCoo - stablizer[1]) / (stablizer[3] - stablizer[1]))

    xCoo = xCoo * 1600 + 150
    yCoo = yCoo * 900 + 80

    for i in range(len(xCoo)):
        cv2.circle(blackBox,(int(xCoo[i]),int(yCoo[i])),20,(0,255,0), 3)

    for i in range(len(notSD)):
        cv2.line(blackBox, (int(xCoo[notSD[i][0]]), int(yCoo[notSD[i][0]])), (int(xCoo[notSD[i][1]]), int(yCoo[notSD[i][1]])), (0, 0, 255), thickness= 10)
        cv2.circle(blackBox,(int(xCoo[notSD[i][0]]),int(yCoo[notSD[i][0]])),20,(0,255,255), 3)
    return img, blackBox,stablizer,sBool