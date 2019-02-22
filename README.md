# coco_keypoints  

ROS package to publish COCO_ARR message that store coco_keypoints  
in order to estimate 3d poses in ROS pakage openpose_skeleton_3d.
### Topics
Subscribe: /pose_estimator/pose  
Publish:  /coco__keypoints/pose 

### Installation
Cloning this repository under src folder in your ros workstation.
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/KeishiIshihara/coco_keypoints.git
```
### Prerequired
tf-pose-estimation for ROS

### Run
```bash
$ rosrun coco_keypoints sample.py
```