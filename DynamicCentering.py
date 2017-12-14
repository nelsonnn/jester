import os
import sys
from Bybop_Discovery import *
import Bybop_Device


#drone.send_data('ardrone3.Piloting.PCMD', flag, roll, pitch, yaw, gaz, timestamp)

def Centering(drone,LeftDot,CenterDotX,CenterDotY,RightDot,Width): #inputs are the center coordinates and Width of face
    if (CenterDot-LeftDot) > (RightDot-CenterDot): #Drone is too far Left
        Ratio = (CenterDot-LeftDot)/(RightDot-CenterDot)
        drone.send_data('ardrone3.Piloting.PCMD', False, Ratio*50, 0, 0, 0, 0)
    elif (CenterDot-LeftDot) < (RightDot-CenterDot): #Drone is too far right
        Ratio = (CenterDot-LeftDot)/(RightDot-CenterDot)
        drone.send_data('ardrone3.Piloting.PCMD', False, Ratio*-50, 0, 0, 0, 0)
        
    if Width > 50: #Drone is too close to face
        drone.send_data('ardrone3.Piloting.PCMD', False, 0, -50, 0, 0, 0)
    elif Width < 50: #Drone is too far from face
        drone.send_data('ardrone3.Piloting.PCMD', False, 0, 50, 0, 0, 0)
        
    if CenterDotY > 330: #Drone too low
        HeightRatio = CenterDoty/330
        drone.send_data('ardrone3.Piloting.PCMD', False, 0, 0, 0, HeightRatio*50, 0)
    elif CenterDotY < 330: #Drone too high
        HeightRatio = 330/CenterDoty
        drone.send_data('ardrone3.Piloting.PCMD', False, 0, 0, 0, HeightRatio*-50, 0)
