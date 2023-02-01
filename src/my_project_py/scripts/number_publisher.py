#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from std_srvs.srv import Empty

class NumberPublisher:

    def __init__(self):
        self.number = 3.1
        self.publisher_interval = 1.5
        self.reset_interval = 7

        self.number_publisher = rospy.Publisher("/number", Float64, queue_size=10)
        
        self.timer_pub = rospy.Timer(rospy.Duration(self.publisher_interval), self.timer_callback)
        self.timer_reset = rospy.Timer(rospy.Duration(self.reset_interval), self.reset_callback)
        
        self.client_reset = rospy.ServiceProxy("reset_counter", Empty, )

        rospy.loginfo("Inicialized")

    def timer_callback(self, event):
        msg = Float64()
        msg.data = self.number
        self.number_publisher.publish(msg)
        rospy.loginfo("Published value: " + str(msg.data))
    
    def reset_callback(self, event):
        rospy.loginfo("Solicitação de reset da contagem")
        self.client_reset()
        
        

if __name__ == '__main__':
    try:
        rospy.init_node("number_publisher_node")
        NumberPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass