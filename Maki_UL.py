from pyax12.connection import Connection
import time
# Connect to the serial port
serial_connection = Connection(port='COM3', baudrate=1000000)
dynamixel_id =4 #eye yaw
dynamixel_id_2 =30 #torso
dynamixel_id_3 =13 #neck
dynamixel_id_4 =40 #eye pitch
dynamixel_id_5 = 6 #neck pitch
dynamixel_id_6 =5 #left eyelid pitch
dynamixel_id_7 =7 #right eyelid pitch


# Go to +10° (moves eyes to the right)
serial_connection.goto(dynamixel_id, -13, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_3, 0, speed=80, degrees=True)
serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_5, 10, speed=75, degrees=True)
time.sleep(3) # Wait 1 second


#Goes to the 0 degree mark (moves eyes to the middle)
serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
time.sleep(.35) # Wait 1 second
