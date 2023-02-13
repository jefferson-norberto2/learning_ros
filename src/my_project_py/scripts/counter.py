#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from std_srvs.srv import Empty, EmptyResponse

class Counter:
    def __init__(self):
        self.count = rospy.get_param("initial_count", 0)
        self.pub_interval = rospy.get_param("~pub_rate", 3)

        rospy.set_param("~custom_param", False)

        if (rospy.has_param("initial_count") or rospy.has_param("~pub_rate")):
            rospy.logwarn("Parametros customizados")
            rospy.set_param("~custom_param", True)
        
        if rospy.get_param("~delete_param", False):
            rospy.logwarn("Deletando parametros")
            if rospy.has_param("~pub_rate"):
                rospy.delete_param("~pub_rate")
            if rospy.has_param("initial_count"):
                rospy.delete_param("initial_count")
             

        # nome do tópico, tipo de mensagen e a função callback e pode definir o tamanho do buffer
        self.num_sub = rospy.Subscriber("/number", Float64, self.number_callback, queue_size=10)
        self.count_pub = rospy.Publisher("/current_count", Float64, queue_size=10)
        self.timer_pub = rospy.Timer(rospy.Duration(self.pub_interval), self.timer_callback)
        self.reset_srv = rospy.Service("reset_counter", Empty, self.reset_srv_callback)
        rospy.loginfo("Counter inicialized")
    
    def number_callback(self, msg):
        self.count = self.count + msg.data
        rospy.loginfo("The current counter: " + str(self.count))
    
    def timer_callback(self, event):
        msg = Float64()
        msg.data = self.count
        self.count_pub.publish(msg)
    
    def reset_srv_callback(self, request):
        self.count = 0
        rospy.loginfo("Reseted count")
        return EmptyResponse()

if __name__ == '__main__':
    try:
        rospy.init_node("counter_node")
        Counter()
        rospy.spin()
    except rospy.ROSInterruptException as interrupt:
        rospy.logerr("Error in node number:" + interrupt)