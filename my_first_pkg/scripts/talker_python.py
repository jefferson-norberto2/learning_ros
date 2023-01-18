#!/usr/bin/env python3

import rospy
from std_msgs.msg import String 

def talker():
    rospy.init_node("talker_python")
    loop_rate = rospy.Rate(10)

    # chatter_pub = rospy.Publisher("chatter", String, queue_size=100)
    # ao colocar o ~ ele pega o nome do contexto geral (/talker_python/chatter)
    chatter_pub = rospy.Publisher("~chatter", String, queue_size=100)

    count = 0
    while not rospy.is_shutdown():
        #fazer alguma coisa
        txt = "Ola ROS World: " + str(count)
        rospy.loginfo(txt)
        chatter_pub.publish(txt)
        loop_rate.sleep()
        count += 1




if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException as e:
        print("Error talker_python:", e)
    