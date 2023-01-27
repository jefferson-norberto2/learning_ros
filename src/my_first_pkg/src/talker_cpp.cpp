#include "ros/ros.h"
#include "std_msgs/String.h"
#include <string>

int main(int argc, char **argv){

    ros::init(argc, argv, "talker_cpp"); // Inicializou o nó
    ros::NodeHandle nh; // registrou no nodehandle
    ros::Rate loopRate(10); // definiu o loopRate para 10 hz

    ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chatter", 1000); 
    // objeto para publicar em um tópico, chatter é o nome, 1000 é o buffer

    int count = 0;
    while (ros::ok()){
        // Mostrar texto no terminal e publicar no tópico
        std::string text = "Ola mundo do Ros! Contando: " + std::to_string(count);
        ROS_INFO("%s", text.c_str()); // usado para mostrar no terminal

        std_msgs::String msg;
        msg.data = text;
        chatter_pub.publish(msg);

        ros::spinOnce(); // atualizar todas as questões do no
        loopRate.sleep(); // over rate
        ++count;
    }
    

    return 0;
}