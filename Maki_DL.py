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

#Goes to -10 degree mark (moves eyes to the left)
serial_connection.goto(dynamixel_id, -13, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_3, 0, speed=80, degrees=True)
serial_connection.goto(dynamixel_id_4, -105, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_5, -25, speed=75, degrees=True)
time.sleep(3) # Wait 1 second


#Goes to the 0 degree mark (moves eyes to the middle)
serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
