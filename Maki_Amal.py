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





while True:
	# Go to +10° (moves eyes to the right)
	serial_connection.goto(dynamixel_id, 13, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 150, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


	# Go to -45° (-45° CCW)
	serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


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


	# Go to +10° (moves eyes to the right)
	serial_connection.goto(dynamixel_id, -13, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 0, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


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



	#Goes to -10 degree mark (moves eyes to the left)
	serial_connection.goto(dynamixel_id, -13, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second

	#Moves base  
	serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +45° (45° CCW)
	serial_connection.goto(dynamixel_id_2, 45, speed=75, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +90° (90° CCW)
	serial_connection.goto(dynamixel_id_2, 90, speed=75, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +135° (135° CCW)
	serial_connection.goto(dynamixel_id_2, 135, speed=75, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +150° (150° CCW)
	serial_connection.goto(dynamixel_id_2, 150, speed=75, degrees=True)
	time.sleep(.25) # Wait 2 seconds

	#Turns head to left shoulder
	serial_connection.goto(dynamixel_id_3, 0, speed=80, degrees=True)
	time.sleep(.60) # Wait 1 second


	serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to -45° (-45° CCW)
	serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
	time.sleep(.60) # Wait 1 second
	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second



	# Go to +10° (moves eyes to the right)
	serial_connection.goto(dynamixel_id, 13, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 150, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -105, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second



	# Go to -70° (moves eyes midway)
	serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second
	# Go to -90° (moves eyed down)
	serial_connection.goto(dynamixel_id_4, -105, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second

	# Goes to 0 degrees (nods head midway)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second
	# Go to -25° (move head forward)
	serial_connection.goto(dynamixel_id_5, -25, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


	# Goes to 0 degrees (nods head midway)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second
	# Go to -70° (moves eyes midway)
	serial_connection.goto(dynamixel_id_4, -70, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second



	#Goes to -10 degree mark (moves eyes to the left)
	serial_connection.goto(dynamixel_id, -13, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 0, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -105, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second


	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id, 0, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=80, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=75, degrees=True)
	time.sleep(.35) # Wait 1 second



	#Turns head to left shoulder
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -80, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 75, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -30, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 30, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -45° (-45° CCW)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
	#serial_connection.goto(dynamixel_id_6, -80, speed=200, degrees=True)
	#serial_connection.goto(dynamixel_id_7, 75, speed=200, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	#serial_connection.goto(dynamixel_id_6, -30, speed=200, degrees=True)
	#serial_connection.goto(dynamixel_id_7, 30, speed=200, degrees=True)
	time.sleep(.1) # Wait 1 second

	
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -30, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 30, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -45° (-45° CCW)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -80, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 75, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -30, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 30, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	#Turns head to left shoulder
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	#serial_connection.goto(dynamixel_id_6, -80, speed=200, degrees=True)
	#serial_connection.goto(dynamixel_id_7, 75, speed=200, degrees=True)
	time.sleep(.1) # Wait 1 second
	
	
	
	#Turns head to left shoulder
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -80, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 75, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id_6, -30, speed=150, degrees=True)
	serial_connection.goto(dynamixel_id_7, 30, speed=150, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -45° (-45° CCW)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
	#serial_connection.goto(dynamixel_id_6, -80, speed=200, degrees=True)
	#serial_connection.goto(dynamixel_id_7, 75, speed=200, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to -150° (turns head/neck to right shoulder)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	#serial_connection.goto(dynamixel_id_6, -30, speed=200, degrees=True)
	#serial_connection.goto(dynamixel_id_7, 30, speed=200, degrees=True)
	time.sleep(.1) # Wait 1 second


	serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to -45 (45 CW)
	serial_connection.goto(dynamixel_id_2, -45, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to -90 (90 CW)
	serial_connection.goto(dynamixel_id_2, -90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, -13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to -135 (135 CW)
	serial_connection.goto(dynamixel_id_2, -135, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 13, speed=50, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to -150 (150 CW)
	serial_connection.goto(dynamixel_id_2, -150, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +150 (150 CCW)
	serial_connection.goto(dynamixel_id_2, 150, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	time.sleep(.25) # Wait 2 seconds
	# Go to +135 (135 CCW)
	serial_connection.goto(dynamixel_id_2, 135, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, -13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +90 (90 CCW)
	serial_connection.goto(dynamixel_id_2, 90, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 13, speed=50, degrees=True)
	time.sleep(.25) # Wait 1 second
	# Go to +45 (45 CCW)
	serial_connection.goto(dynamixel_id_2, 45, speed=75, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	time.sleep(.25) # Wait 1 second
	#Moves base 
	serial_connection.goto(dynamixel_id_2, 0, speed=75, degrees=True)
	time.sleep(.1) # Wait 1 second



	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=50, degrees=True)
	time.sleep(.40) # Wait 1 second
	#Goes to -10 degree mark (moves eyes to the left)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, -13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -105, speed=40, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to +10 (moves eyes to the right)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=40, degrees=True)
	time.sleep(.40) # Wait 1 second
	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=40, degrees=True)
	time.sleep(.1) # Wait 1 second

	

	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=40, degrees=True)
	time.sleep(.40) # Wait 1 second
	# Go to +10 (moves eyes to the right)
	serial_connection.goto(dynamixel_id_3, 150, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 10, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -90, speed=40, degrees=True)
	time.sleep(.40) # Wait 1 second
	#Goes to -10 degree mark (moves eyes to the left)
	serial_connection.goto(dynamixel_id_3, 75, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, -25, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, -13, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -105, speed=40, degrees=True)
	time.sleep(.40) # Wait 1 second
	#Goes to the 0 degree mark (moves eyes to the middle)
	serial_connection.goto(dynamixel_id_3, 0, speed=40, degrees=True)
	serial_connection.goto(dynamixel_id_5, 0, speed=35, degrees=True)
	serial_connection.goto(dynamixel_id, 0, speed=50, degrees=True)
	serial_connection.goto(dynamixel_id_4, -70, speed=40, degrees=True)
	time.sleep(.35) # Wait 1 second

