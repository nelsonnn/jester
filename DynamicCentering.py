import os
import sys

sys.path.append('/Users/nelson/Desktop/Programs/bybop/src')

from Bybop_Discovery import *
import Bybop_Device


#drone.send_data('ardrone3.Piloting.PCMD', flag, roll, pitch, yaw, gaz, timestamp)

def Centering(drone, LeftDot, CenterDotX, CenterDotY, RightDot, Width, face_centerX, face_centerY):
    yaw_C = 15
    roll_C = 20
    pitch_C = 20
    gaz_C = 20

    flag = False
    roll = 0
    pitch = 0
    yaw = 0
    gaz = 0

    # ##ROLL##
    # if (CenterDotX-LeftDot) > (RightDot-CenterDotX): #Drone is too far Left
    #
    #     if RightDot-CenterDotX > 1:
    #         roll = int((CenterDotX - LeftDot) / (RightDot - CenterDotX) * roll_C)
    #         if roll > 100:
    #             roll = 100
    #
    #     else:
    #         roll = 100
    #
    # if (CenterDotX-LeftDot) < (RightDot-CenterDotX): #Drone is too far right
    #
    #     if RightDot-CenterDotX > 1:
    #         roll = int( (RightDot - CenterDotX) / (CenterDotX - LeftDot) * (-roll_C))
    #         if roll < -100:
    #             roll = -100
    #
    #     else:
    #         roll = -100

    ##YAW##
    if face_centerX < 250: # Drone is too far right

        roll = int(250/face_centerX * roll_C)

        if roll > 100:
            roll = 100

    if face_centerX > 250: # Drone is too far left

        roll = int(face_centerX/250 * (-roll_C))

        if roll < -100:
            roll = -100

    ##PITCH##
    if Width > 45:  # Drone is too close to face
        pitch = int(Width/50)*(-pitch_C)
        if pitch < -10:
            pitch = -10

    if Width < 45:  # Drone is too far from face
        pitch = int(50/Width)*pitch_C
        if pitch > 10:
            pitch = 10

    ##GAZ##
    if face_centerY > 110: #Drone too high

        gaz = int(face_centerY/140 * (-gaz_C))

        if gaz < -100:
            gaz = -100

    if face_centerY < 110: #Drone too low

        gaz = int(140/face_centerY * gaz_C)

        if gaz > 100:
            gaz = 100
    #

    if roll != 0 or pitch != 0:
        flag = True

    print("Roll: {0}, Pitch: {1}, Yaw: {2}, Gaz: {3}".format(roll, pitch, yaw, gaz))
    drone.send_data('ardrone3.Piloting.PCMD', flag, roll, pitch, yaw, gaz, 0)