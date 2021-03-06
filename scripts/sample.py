#!/usr/bin/env python
import rospy
import sys
import numpy as np
from coco_keypoints.msg import COCO
from coco_keypoints.msg import COCO_ARR
from tfpose_ros.msg import Persons
from tfpose_ros.msg import BodyPartElm

class PublishCoco:
    def __init__(self):
        # self.pub = rospy.Publisher('/coco_keypoints/pose', COCO_ARR, queue_size=10)
	self.num = 19


    def set_body_parts(self, data):
	body_parts = BodyPartElm()
	body_parts.part_id = -1
	body_parts.x = -1
	body_parts.y = -1
	body_parts.confidence = -1
        np_body_part_id = np.full(19, -1)
	np_body_parts = np.full(19, body_parts)
	
        for i in range(len(data)):
            np_body_part_id[data[i].part_id] = data[i].part_id
            np_body_parts[data[i].part_id] = data[i]
	    # print "----"
	    # print data[i].part_id
        return np_body_part_id, np_body_parts


    def publishDetectionPose(self, persons, pose):
            coco_arr = COCO_ARR()
            coco_arr.header = pose.header
            coco_arr.num_person = persons.size
	    print "person.size: "+str(persons.size)
            for i in range(persons.size):
		# print "i: "+str(i)
            	coco = COCO()
                body_list, data = self.set_body_parts(persons[i].body_part)
		for j in range(len(data)):
			data[j].x *= pose.image_w
			data[j].y *= pose.image_h

		# print data[1]
		# print body_list
                if body_list[0] != -1:
                    coco.Nose.x = data[0].x
                    coco.Nose.y = data[0].y
                    coco.Nose.confidence = data[0].confidence
		    # print "data[0]: "+str(data[0])
                if body_list[1] != -1:
                    coco.Neck.x = data[1].x
                    coco.Neck.y = data[1].y
                    coco.Neck.confidence = data[1].confidence
            
                if body_list[2] != -1:
                    coco.RShoulder.x = data[2].x
                    coco.RShoulder.y = data[2].y
                    coco.RShoulder.confidence = data[2].confidence

                if body_list[3] != -1:
	                coco.RElbow.x = data[3].x
	                coco.RElbow.y = data[3].y
	                coco.RElbow.confidence = data[3].confidence


	        if body_list[4] != -1:
	                coco.RWrist.x = data[4].x
	                coco.RWrist.y = data[4].y
	                coco.RWrist.confidence = data[4].confidence

	        if body_list[5] != -1:
	                coco.LShoulder.x = data[5].x
	                coco.LShoulder.y = data[5].y
	                coco.LShoulder.confidence = data[4].confidence
	            
	        if body_list[6] != -1:
	                coco.LElbow.x = data[6].x
	                coco.LElbow.y = data[6].y
	                coco.LElbow.confidence = data[6].confidence
	            
	        if body_list[7] != -1:
	                coco.LWrist.x = data[7].x
	                coco.LWrist.y = data[7].y
	                coco.LWrist.confidence = data[7].confidence
	            
	        if body_list[8] != -1:
	                coco.RHip.x = data[8].x
	                coco.RHip.y = data[8].x
	                coco.RHip.confidence = data[8].confidence
	            
	        if body_list[9] != -1:
	                coco.RKnee.x = data[9].x
	                coco.RKnee.y = data[9].y
	                coco.RKnee.confidence = data[9].confidence
	            
	        if body_list[10] != -1:
	                coco.RAnkle.x = data[10].x
	                coco.RAnkle.y = data[10].y
	                coco.RAnkle.confidence = data[10].confidence
	            
	        if body_list[11] != -1:
	                coco.LHip.x = data[11].x
	                coco.LHip.y = data[11].y
	                coco.LHip.confidence = data[11].confidence
	            
	        if body_list[12] != -1:
	                coco.LKnee.x = data[12].x
	                coco.LKnee.y = data[12].y
	                coco.LKnee.confidence = data[12].confidence
	            
	        if body_list[13] != -1:
	                coco.LAnkle.x = data[13].x
	                coco.LAnkle.y = data[13].y
	                coco.LAnkle.confidence = data[13].confidence
	            
	        if body_list[14] != -1:
	                coco.REye.x = data[14].x
	                coco.REye.y = data[14].y
	                coco.REye.confidence = data[14].confidence
	            
	        if body_list[15] != -1:
	                coco.LEye.x = data[15].x
	                coco.LEye.y = data[15].y
	                coco.LEye.confidence = data[15].confidence
	            
	        if body_list[16] != -1:
	                coco.REar.x = data[16].x
	                coco.REar.y = data[16].y
	                coco.REar.confidence = data[16].confidence
	            
	        if body_list[17] != -1:
	                coco.LEar.x = data[17].x
	                coco.LEar.y = data[17].y
	                coco.LEar.confidence = data[17].confidence
	            
	        if body_list[18] != -1:
	                coco.Waist.x = data[18].x
	                coco.Waist.y = data[18].y
	                coco.Waist.confidence = data[18].confidence
	        coco_arr.data.append(coco)
		print coco_arr

            self.pub.publish(coco_arr)
        

        # coco_arr.data.emplace_back(coco)


    def callback(self, pose):
            rate = rospy.Rate(10)
            body_list = np.full(19, -1)
            self.pub = rospy.Publisher('/coco_keypoints/pose', COCO_ARR, queue_size=10)	    
			# print (pose.persons[0].body_part[0])
            print "------------------------------------"
            persons = np.array(pose.persons)
            print "image_w: "+str(pose.image_w)
            print "image_h: "+str(pose.image_h)
			# print "---------------------"
			# print data.shape 
			# print data.ndim
			# print data.size
			# print data[1]
			# print data[1].part_id
			# print "-- last one --"
			# print data[data.size-1]
			# print ""
            
            self.publishDetectionPose(persons, pose)
            # rospy.sleep(1.0)

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
	
