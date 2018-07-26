import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
class pad_cmd_vel:
    def __init__(self):
        rospy.init_node('pad_cmd_vel')
        self.joy_sub=rospy.Subscriber('joy',Joy,self.joy_callback,queue_size=1)
        self.twist_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
        rospy.spin()
    def joy_callback(self,joy_msg):
        twist=Twist();
        twist.linear.x=joy_msg.axes[1]
        twist.linear.y=joy_msg.axes[0]

        twist.angular.z=joy_msg.axes[3]

        self.twist_pub.publish(twist)

pad=pad_cmd_vel();
