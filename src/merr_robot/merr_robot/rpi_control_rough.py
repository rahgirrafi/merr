import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from geometry_msgs.msg import Twist # Message type for publishing velocity commands
import RPi.GPIO as GPIO # Library for GPIO control
from RPi.GPIO import PWM # Library for PWM control




class RPiControl(Node):

    def __init__(self):
        super().__init__('rpi_control')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.lpwm = PWM(12, 300) # Left Motor PWM
        self.rpwm = PWM(13, 300) # Right Motor PWM
        self.speed = 100

    def listener_callback(self, msg:Twist):
        self.get_logger().info('Linear: %f, Angular: %f' % (msg.linear.x, msg.angular.z))
        self.x = msg.linear.x
        # self.y = msg.linear.y
        # self.z = msg.linear.z
        # self.roll = msg.angular.x
        # self.pitch = msg.angular.y
        self.yaw = msg.angular.z

        #map x and yaw to motor commands of differential bot
        if self.yaw>0:
            self.diffbot.set_speed(self.lpwm(self.speed*(self.x - self.yaw)), self.x * self.speed)
            self.get_logger().info('Turning right at speed %f' % self.speed)

        else:
            self.diffbot.set_speed(self.lpwm.ChangeDutyCycle(self.x * self.speed), self.rpwm.ChangeDutyCycle(self.speed*(self.x - self.yaw)))
            self.get_logger().info('Turning left at speed %f' % self.speed)


def main(args=None):
    rclpy.init(args=args)

    rpi_control = RPiControl()  
    rclpy.spin(rpi_control)
    rpi_control.destroy_node()  
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()