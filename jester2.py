from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
from DroneStartup import ConnectToDrone
from DynamicCentering import Centering

OUTPUT_SIZE_WIDTH = 775
OUTPUT_SIZE_HEIGHT = 600
rectangleColor = (0,165,255)

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#Open the first webcame device
capture = cv2.VideoCapture(0)

#Create two opencv named windows
cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)

#Position the windows next to eachother
cv2.moveWindow("base-image",0,100)
cv2.moveWindow("result-image",400,100)

#Start the window thread for the two windows we are using
cv2.startWindowThread()

drone = ConnectToDrone()
drone.take_off()

while True:
    #Retrieve the latest image from the webcam
    rc,fullSizeBaseImage = capture.read()

    #Resize the image
    baseImage = imutils.resize(fullSizeBaseImage, width=500)

    #Check if a key was pressed and if it was Q, then destroy all
    #opencv windows and exit the application
    pressedKey = cv2.waitKey(2)
    if pressedKey == ord('Q'):
        cv2.destroyAllWindows()
        # drone.land()
        # drone.stop()
        exit(0)



    #Result image is the image we will show the user, which is a
    #combination of the original image from the webcam and the
    #overlayed rectangle for the largest face
    resultImage = baseImage.copy()


    #For the face detection, we need to make use of a gray colored
    #image so we will convert the baseImage to a gray-based image
    gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
    #Now use the haar cascade detector to find all faces in the
    #image
    faces = detector(gray, 1)

    #for finding the biggest face
    maxarea = 0
    x = 0
    y = 0
    w = 0
    h = 0

    for(i, face) in enumerate(faces):

        # determine the facial landmarks for the face region
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)


        (x_, y_, w_, h_) = face_utils.rect_to_bb(face)
        cv2.rectangle(resultImage, (x_,y_), (x_ + w_, y_ + h_), rectangleColor)
        for (x_, y_) in shape:
            cv2.circle(resultImage, (x_, y_), 1, (0, 0, 255), -1)
        if w_ * h_ > maxarea:
            maxarea = w_ * h_
            x = x_
            y = y_
            w = w_
            h = h_
    # if maxarea > 0:
    #     if x > 300:
            #drone.send_data('ardrone3.Piloting.PCMD', False, 0, 0, 50, 0, 0)
    Centering(drone,shape[2][0],shape[30][0],shape[0][1],shape[14][0],w)

    #Since we want to show something larger on the screen than the
    #original 320x240, we resize the image again
    #
    #Note that it would also be possible to keep the large version
    #of the baseimage and make the result image a copy of this large
    #base image and use the scaling factor to draw the rectangle
    #at the right coordinates.
    largeResult = cv2.resize(resultImage,
                 (OUTPUT_SIZE_WIDTH,OUTPUT_SIZE_HEIGHT))

    #Finally, we want to show the images on the screen
    cv2.imshow("base-image", baseImage)
    cv2.imshow("result-image", largeResult)



    ###########################################################
    #Drone control
    
