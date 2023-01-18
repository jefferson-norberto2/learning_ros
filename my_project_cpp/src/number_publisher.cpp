// Nó que fica publicando no contador em uma determinada frequencia

#include "ros/ros.h"
#include "std_msgs/Float64.h"

class NumberPublisher{                            

    public:
        NumberPublisher(ros::NodeHandle *nh){     
            //Inicializar Variaveis
            number = 1.2;
            pub_interval = 1;

            num_pub = nh->advertise<std_msgs::Float64>("/number", 10);
            timer_pub = nh->createTimer(ros::Duration(pub_interval), &NumberPublisher::timerCallback, this);

        }

        void timerCallback(const ros::TimerEvent &event){
            std_msgs::Float64 msg;
            msg.data = this->number;
            num_pub.publish(msg);
        }

    private:
        double number;
        double pub_interval;
        ros::Publisher num_pub;
        ros::Timer timer_pub;

};


int main(int argc, char **argv)
{
    ros::init(argc, argv, "number_publisher");     
    ros::NodeHandle nh;
    NumberPublisher number_publisher = NumberPublisher(&nh);    
    
    ros::spin();
    return 0;
}