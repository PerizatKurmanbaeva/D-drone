#!/usr/bin/env python

# PPM_to_servo.py
# 2019-10-09
# Public Domain

# after reboot do 
# sudo pigpiod

import time
import pigpio # http://abyz.me.uk/rpi/pigpio/python.html
import rospy
from std_msgs.msg import String
import json


def paint(msg):
	pi = pigpio.pi()
	if not pi.connected:
	   exit()

	msg = str(msg).replace('"', '').split()[1]
	print msg
	if (msg == 'down'):
		pi.set_servo_pulsewidth(23, 2000)
	else:
		pi.set_servo_pulsewidth(23, 500) # ~0
	time.sleep(0.4)
	pi.set_servo_pulsewidth(23, 0)
	pi.stop()
	time.sleep(0.2)

rospy.init_node('painter')
# painter = rospy.Publisher('/paint', String, queue_size=1)
# painter.publish(data='hello world')
rospy.Subscriber('/paint', String, paint)
# time.sleep(10)
# painter.publish(data='hello world')
rospy.spin()
