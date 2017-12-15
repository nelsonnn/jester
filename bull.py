from DroneStartup import ConnectToDrone
from time import sleep
drone = ConnectToDrone()

drone.take_off()

sleep(5)

drone.send_data('ardrone3.Piloting.PCMD', False, 0, 0, 70, 50, 0)
drone.send_data('ardrone3.Piloting.PCMD', False, 0, 0, -70, -50, 0)
sleep(5)

drone.land()

sleep(5)

drone.stop()

exit()