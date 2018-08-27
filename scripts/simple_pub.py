#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def simple_pub():
    pub = rospy.Publisher("spub", String, queue_size = 10)
    rospy.init_node("simple_pub")
    rate = rospy.Rate(2) # 2 Hz
    while not rospy.is_shutdown():
        pubStr = "simple_pub %s" % (rospy.get_time())
        rospy.loginfo(pubStr)
        pub.publish(pubStr)
        rate.sleep()

if __name__ == "__main__":
    try:
        simple_pub()
    except rospy.ROSInterruptException:
        pass
