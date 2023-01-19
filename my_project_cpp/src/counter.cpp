#include "ros/ros.h"

// Mensagens
#include "std_msgs/Float64.h"

// ELE VAI CRIAR UM SUBCRIVE, CADA VEZ QUE TIVER UMA NOVA PUB NO NUMBER
// ELE VAI SOMAR NO COUNT
class Counter{
    //Metodos publicos
    public:
        // o * diz que estou passando o ponteiro
        Counter(ros::NodeHandle *nh){
            count = 0;
            publish_interval = 1;
            num_sub = nh->subscribe("/number", 10, &Counter::numberCallback, this);
            count_pub = nh->advertise<std_msgs::Float64>("/current_counter", 10);
            timer_pub = nh->createTimer(ros::Duration(publish_interval), &Counter::timerCallback, this);
            
            ROS_INFO("Inicialited Counter_node");
        }

        // O símbolo & diz que estou passando por referência
        void numberCallback(const std_msgs::Float64 &msg){
            // Em java seria this.count
            this->count = this->count + msg.data;
            ROS_INFO("Contagem atual %f", count);
        }

        // Função para ficar publicando o contador
        void timerCallback(const ros::TimerEvent &event){
            std_msgs::Float64 msg;
            msg.data = this->count;
            count_pub.publish(msg);
        }

    //Metodos privados
    private:
        double count;
        double publish_interval;
        ros::Subscriber num_sub;
        ros::Publisher count_pub;
        ros::Timer timer_pub;
};

int main(int argc, char **argv){
    // inicializar o nó
    ros::init(argc, argv, "counter_node");
    //criar o nodehandle
    ros::NodeHandle nh;

    Counter counter = Counter(&nh);
    ros::spin();

    return 0;
}