#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class Counter:
    def __init__(self):
        self.count = 0
        self.pub_interval = 3
        # nome do tópico, tipo de mensagen e a função callback e pode definir o tamanho do buffer
        self.num_sub = rospy.Subscriber("/number", Float64, self.number_callback, queue_size=10)
        self.count_pub = rospy.Publisher("/current_count", Float64, queue_size=10)
        self.timer_pub = rospy.Timer(rospy.Duration(self.pub_interval), self.timer_callback)
        rospy.loginfo("Counter inicialized")
    
    def number_callback(self, msg):
        self.count = self.count + msg.data
        rospy.loginfo("The current counter: " + str(self.count))
    
    def timer_callback(self, event):
        msg = Float64()
        msg.data = self.count
        self.count_pub.publish(msg)

if __name__ == '__main__':
    try:
        rospy.init_node("counter_node")
        Counter()
        rospy.spin()
    except rospy.ROSInterruptException as interrupt:
        rospy.loginfo("Error in node number:" + interrupt)