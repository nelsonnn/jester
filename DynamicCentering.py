import os
import sys
from Bybop_Discovery import *
import Bybop_Device



def Centering(Xcenter,Ycenter,Width): #inputs are the center coordinates and Width of face
    if Width > 50: #Drone is too close to face
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,0)
    elif Width < 50: #Drone is too far from face
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,0)
    if Xcenter > 388: #Face is to the right of drone's vision
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,-1)
    elif Xcenter < 388: #Face is to the left of drone's vision
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,1)
    if Ycenter > 250: #Face is to the top of drone's vision
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,0)
    elif Ycenter < 250: #Face is to the bottom of drone's vision
        drone.send_data('aRDrone3.Piloting.sendPilotingMoveBy',0,0,0,0)
