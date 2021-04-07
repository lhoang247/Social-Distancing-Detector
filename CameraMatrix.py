import cv2
import numpy as np
def returnCameraParameters(cameraNum):

    if (cameraNum == 1):
        rvec =  np.matrix([1.759099006652832,0.46710100769996643 ,-0.331699013710022])
        tvec = np.matrix([525.8941650390625 ,45.40763473510742 ,986.7235107421875])
        cameraMatrix = np.matrix([1743.4478759765625,0.0,934.5202026367188,0.0,1735.1566162109375,444.3987731933594,0.0,0.0,1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.43248599767684937, 0.6106230020523071, 0.008233999833464622, 0.0018599999602884054, -0.6923710107803345])
    elif (cameraNum == 2):
        rvec =  np.matrix([ 0.6167870163917542, -2.14595890045166, 1.6577140092849731])
        tvec = np.matrix([1195.231201171875, -336.5144958496094, 2040.53955078125])
        cameraMatrix = np.matrix([1707.266845703125, 0.0, 978.1306762695312, 0.0, 1719.0408935546875, 417.01922607421875, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.2190140038728714, -0.31163400411605835, 0.008686999790370464, 0.0003589999978430569, 0.6136000156402588])
    elif (cameraNum == 3):
        rvec =  np.matrix([0.5511789917945862, 2.229501962661743, -1.7721869945526123])
        tvec = np.matrix([55.07157897949219, -213.2444610595703, 1992.845703125])
        cameraMatrix = np.matrix([1738.7144775390625, 0.0, 906.56689453125, 0.0, 1752.8876953125, 462.0346374511719, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.2952420115470886, -0.9262599945068359, 0.015855999663472176, -0.0010989999864250422, 4.333065986633301])
    elif (cameraNum == 4):
        rvec =  np.matrix([1.6647210121154785, 0.9668620228767395, -0.6937940120697021])
        tvec = np.matrix([42.36193084716797, -45.360652923583984, 1106.8572998046875])
        cameraMatrix = np.matrix([1725.2772216796875, 0.0, 995.0142211914062, 0.0, 1720.581787109375, 520.4190063476562, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.5045070052146912, 0.761011004447937, 0.0010519999777898192, 0.0028979999478906393, -0.597877025604248])
    elif (cameraNum == 5):
        rvec =  np.matrix([1.2132920026779175, -1.4771349430084229, 1.2775369882583618])
        tvec = np.matrix([836.6625366210938, 85.86837005615234, 600.2880859375])
        cameraMatrix = np.matrix([1708.6573486328125, 0.0, 936.0921630859375, 0.0, 1737.1904296875, 465.18243408203125, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.3109759986400604, 0.24370500445365906, 0.011621000245213509, 6.800000119255856e-05, -0.15725000202655792])
    elif (cameraNum == 6):
        rvec =  np.matrix([1.6907379627227783, -0.3968360126018524, 0.355197012424469])
        tvec = np.matrix([-338.5532531738281, 62.87659454345703, 1044.094482421875])
        cameraMatrix = np.matrix([1742.977783203125, 0.0, 1001.0738525390625, 0.0, 1746.0140380859375, 362.4325866699219, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.3396880030632019, 0.44677799940109253, 0.028030000627040863, -0.0010710000060498714, -0.5485640168190002])
    elif (cameraNum == 7):
        rvec =  np.matrix([ 1.6439390182495117, 1.126188039779663, -0.7273139953613281])
        tvec = np.matrix([-648.9456787109375, -57.225215911865234, 1052.767578125])
        cameraMatrix = np.matrix([1732.4674072265625, 0.0, 931.2559204101562, 0.0, 1757.58203125, 459.43389892578125, 0.0, 0.0, 1.0])
        cameraMatrix = np.reshape(cameraMatrix, (3,3))
        dist = np.array([-0.3058120012283325, 0.1030540019273758, 0.009813999757170677, 4.8999998398358e-05, 0.15730799734592438])

    R_mat = np.transpose(cv2.Rodrigues(rvec)[0].reshape(3,3))
 
 
    return R_mat,tvec,cameraMatrix,dist