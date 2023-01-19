#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class Counter:
    def __init__(self):
        self.count = 0
        # nome do tópico, tipo de mensagen e a função callback e pode definir o tamanho do buffer
        self.num_sub = rospy.Subscriber("/number", Float64, self.number_callback, queue_size=10)
        rospy.loginfo("Counter inicialized")
    
    def number_callback(self, msg):
        self.count = self.count + msg.data
        rospy.loginfo("The current counter: " + str(self.count))

if __name__ == '__main__':
    try:
        rospy.init_node("counter_node")
        Counter()
        rospy.spin()
    except rospy.ROSInterruptException as interrupt:
        rospy.loginfo("Error in node number:" + interrupt)