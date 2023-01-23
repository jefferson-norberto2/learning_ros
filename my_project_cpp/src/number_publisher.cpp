// Nó que fica publicando no contador em uma determinada frequencia

#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "std_srvs/Empty.h"

class NumberPublisher{                            

    public:
        NumberPublisher(ros::NodeHandle *nh){     
            //Inicializar Variaveis
            number = 1.2;
            pub_interval = 1;
            reset_interval = 7;

            num_pub = nh->advertise<std_msgs::Float64>("/number", 10);
            timer_pub = nh->createTimer(ros::Duration(pub_interval), &NumberPublisher::timerCallback, this);
            client_reset = nh->serviceClient<std_srvs::Empty>("reset_counter");
            timer_reset = nh->createTimer(ros::Duration(reset_interval), &NumberPublisher::resetCallback, this);
        }

        void timerCallback(const ros::TimerEvent &event){
            std_msgs::Float64 msg;
            msg.data = this->number;
            num_pub.publish(msg);
        }

        void resetCallback(const ros::TimerEvent &event){
            std_srvs::Empty srv;
            ROS_INFO("Reset counter solicited");
            client_reset.call(srv);
        }

    private:
        double number;
        double pub_interval;
        double reset_interval;
        ros::Publisher num_pub;
        ros::Timer timer_pub;
        ros::ServiceClient client_reset;
        ros::Timer timer_reset;

};


int main(int argc, char **argv)
{
    ros::init(argc, argv, "number_publisher");     
    ros::NodeHandle nh;
    NumberPublisher number_publisher = NumberPublisher(&nh);    
    
    ros::spin();
    return 0;
}