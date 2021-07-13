#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32, Bool


stop = False
def callback(data):
    global stop 
    stop = data.data

def talker():
    pub = rospy.Publisher('chatter', Float32, queue_size=10)
    rospy.Subscriber("stop_publisher", Bool, callback)
    rospy.init_node('talker', anonymous=True)
    desired_rate = rospy.get_param('~desired_rate')
    rate = rospy.Rate(desired_rate)


    
    while not rospy.is_shutdown():
        if not stop:
            message = random.random()
            rospy.loginfo(message)
            pub.publish(message)
            rate.sleep()
        else:
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass