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

# Go to -70° (moves eyes midway)
serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second

# Go to 0° (move head midway)
serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to 10° (nods head back)
serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
time.sleep(.35) # Wait 1 second

# Go to 0° (move head midway)
serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
# Go to -70° (moves eyes midway)
serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
