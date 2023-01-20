#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class NumberPublisher:

    def __init__(self):
        self.number = 3.1
        self.publisher_interval = 1.5

        self.number_publisher = rospy.Publisher("/number", Float64, queue_size=10)
        self.timer_pub = rospy.Timer(rospy.Duration(self.publisher_interval), self.timer_callback)

        rospy.loginfo("Inicialized")

    def timer_callback(self, event):
        msg = Float64()
        msg.data = self.number
        self.number_publisher.publish(msg)
        
        

if __name__ == '__main__':
    try:
        rospy.init_node("number_publisher_node")
        NumberPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass