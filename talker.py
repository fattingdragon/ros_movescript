#!/usr/bin/env python 
# coding=UTF-8
import rospy   #导入rospy包
from testpy.msg import test
def talker():
	pub = rospy.Publisher('chatter',test)
	rospy.init_node('robot_joint_publisher',anonymous=True)
	r1 = 0
	r2 = 0
	while not rospy.is_shutdown():
		r1 = r1 + 0.01
		r2 = r2 + 0.01
		temp = [joint_base, joint_back] [r1, r2]
		rospy.loginfo(test(temp))
		pub.publish(test(temp))
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
