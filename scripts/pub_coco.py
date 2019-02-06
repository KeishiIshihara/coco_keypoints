#!/usr/bin/env python
import rospy
import sys
import numpy as np
from coco_keypoints.msg import COCO
from tfpose_ros.msg import Persons

class PublishCoco:
	def __init__(self):
		self.pub = rospy.Publisher('coco', coco, queue_size=10)
		self.coco = COCO()


	def switcher(self, part_id):
		coco_map = {
			1 : self.coco.Nose,
			2 : self.coco.Neck,
			3 : self.coco.RShoulder
			}
		try:
			return coco_map[part_id]()
		except KeyError as e:
			raise ValueError('Invalid printer: {}'.format(pose))


	def callback(self, pose):
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			# print (pose.persons[0].body_part[0])
			a = np.array(pose.persons[0].body_part)
			print "----------------------"
			print a.shape
			print a.ndim
			print a.size
			print a[1]
			print a[1].part_id
			print "last one"
			print a[a.size-1]
			print len(pose.persons)
		        
			print ""
			persons = np.array(pose.persons)
			print persons.size
			print persons.shape		
			print persons[0]
			print persons[0].body_part[0]
			print len(persons[0].body_part)
			print a.size
			print persons[0].body_part[0].x

			# print len(pose.persons[0])
		    	# print a[0]

			# print pose.persons[0].body_part[0]
			# for i in pose.persons:
			# 	print i


def main(args):
	pC = PublishCoco()
	rospy.init_node('pubcoco_node', anonymous=True)
	try:
		rospy.Subscriber('/pose_estimator/pose', Persons, pC.callback)
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutting down ROS module"
		del pC

if __name__=='__main__':
	main(sys.argv)
	
