#!/usr/bin/env python

import rospy
import unittest
import rostest
from time import sleep
from std_msgs.msg import Float32

class TalkerTest(unittest.TestCase):
    talker_publishing = False
    def callback(self, data):
        self.talker_publishing = True

    def test_publisher(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Float32, self.callback)

        count = 0
        while not rospy.is_shutdown() and count < 10 and not self.talker_publishing:
            sleep(1)
            count += 1
        self.assertTrue(self.talker_publishing)

if __name__ == '__main__':
    rostest.rosrun('test_package', 'listener', TalkerTest)