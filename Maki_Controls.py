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

#Goes to the 0 degree mark (moves eyes to the middle)
serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
#Goes to -10 degree mark (moves eyes to the left)
serial_connection.goto(dynamixel_id, -10, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to +10° (moves eyes to the right)
serial_connection.goto(dynamixel_id, 10, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
#Goes to the 0 degree mark (moves eyes to the middle)
serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second

#Moves base 
serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
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
# Go to +150° (150° CCW)
serial_connection.goto(dynamixel_id_2, 150, speed=75, degrees=True)
time.sleep(.25) # Wait 2 seconds
# Go to +135° (135° CCW)
serial_connection.goto(dynamixel_id_2, 135, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
# Go to +90° (90° CCW)
serial_connection.goto(dynamixel_id_2, 90, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
# Go to +45° (45° CCW)
serial_connection.goto(dynamixel_id_2, 45, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second
#Moves base 
serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
time.sleep(.25) # Wait 1 second

#Turns head to left shoulder
serial_connection.goto(dynamixel_id_3, 0, speed=75, degrees=True)
time.sleep(.60) # Wait 1 second
# Go to -45° (-45° CCW)
serial_connection.goto(dynamixel_id_3, -45, speed=75, degrees=True)
time.sleep(.60) # Wait 1 second
'''# Go to -90° (-90° CCW)
serial_connection.goto(dynamixel_id_3, -90, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -135° (-135° CCW)
serial_connection.goto(dynamixel_id_3, -135, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -150° (-150° CCW)
serial_connection.goto(dynamixel_id_3, -150, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second'''
# Go to -150° (turns head/neck to right shoulder)
serial_connection.goto(dynamixel_id_3, -150, speed=75, degrees=True)
time.sleep(.60) # Wait 1 second
# Go to -45° (-45° CCW)
serial_connection.goto(dynamixel_id_3, -45, speed=75, degrees=True)
time.sleep(.60) # Wait 1 second

# Go to -70° (moves eyes midway)
serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -90° (moves eyed down)
serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -135° (moves eyes to it's maximum)
serial_connection.goto(dynamixel_id_4, -115, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -70° (moves eyes midway)
serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second


# Goes to 0 degrees (nods head midway)
serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -25° (move head forward)
serial_connection.goto(dynamixel_id_5, -25, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to 10° (nods head back)
serial_connection.goto(dynamixel_id_5, 10, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to 0° (move head midway)
serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second


# Go to -91° (closes eyelid)
serial_connection.goto(dynamixel_id_6, -91, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second'
#opens eyelid midway
serial_connection.goto(dynamixel_id_6, -45, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second'
# Go to -15° (opens eyelid)
serial_connection.goto(dynamixel_id_6, -15, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second

#Goes to +75 degrees (closes eyelid)
serial_connection.goto(dynamixel_id_7, 75, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second
# Goes to +50 degrees(closes eyelid midway)
serial_connection.goto(dynamixel_id_7, 50, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second
# Go to +15° (opens eyelid)
serial_connection.goto(dynamixel_id_7, 15, speed=75, degrees=True)
time.sleep(.50) # Wait 1 second