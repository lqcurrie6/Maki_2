from pyax12.connection import Connection
import time
# Connect to the serial port
serial_connection = Connection(port='COM3', baudrate=1000000)
dynamixel_id =4 #eyes
dynamixel_id_2 =30 #base
dynamixel_id_3 =13 #neck
dynamixel_id_4 =40 #eye lift
dynamixel_id_5 = 6 #nod
dynamixel_id_6 =5 #left eyelid
dynamixel_id_7 =7 #right eyelid

# Go to +10° (moves eyes to the right)
serial_connection.goto(dynamixel_id, 13, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second

#Moves base 
# Go to -45° (45° CW)
serial_connection.goto(dynamixel_id_2, -45, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
# Go to -90° (90° CW)
serial_connection.goto(dynamixel_id_2, -90, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
# Go to -135° (135° CW)
serial_connection.goto(dynamixel_id_2, -135, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
# Go to -150° (150° CW)
serial_connection.goto(dynamixel_id_2, -150, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second

# Go to -150° (turns head/neck to right shoulder)
serial_connection.goto(dynamixel_id_3, 150, speed=80, degrees=True)
time.sleep(.60) # Wait 1 second

serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
time.sleep(.60) # Wait 1 second
#Goes to the 0 degree mark (moves eyes to the middle)
serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second