import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from geometry_msgs.msg import Twist # Message type for publishing velocity commands
import RPi.GPIO as GPIO # Library for GPIO control
from RPi.GPIO import PWM # Library for PWM control


    

class RPiControl(Node):

    def __init__(self):
        super().__init__('rpi_control')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        self.lpwm = PWM(12, 50) # Left Motor PWM
        self.lpwm.start(75)
        self.rpwm = PWM(13, 50) # Right Motor PWM
        self.rpwm.start(75)
        self.speed = 0
        self.left_signal = 0
        self.right_signal = 0

    def listener_callback(self, msg:Twist):
        self.get_logger().info('Linear: %f, Angular: %f' % (self.left_signal, self.right_signal))
        self.x = msg.linear.x 
        # self.y = msg.linear.y
        # self.z = msg.linear.z
        # self.roll = msg.angular.x
        # self.pitch = msg.angular.y
        self.yaw = msg.angular.z

        #map x and yaw to motor commands of differential bot
        self.linear = self.x*25
        self.angular = self.yaw*25

        self.left_signal = max(0,min(100,75+ self.linear - self.angular)) 
        self.right_signal = max(0,min(100,75 + self.linear + self.angular))

        #constrain the values between 0 and 100


        self.lpwm.ChangeDutyCycle(self.left_signal)
        self.rpwm.ChangeDutyCycle(self.right_signal)

def main(args=None):
    rclpy.init(args=args)

    rpi_control = RPiControl()  
    rclpy.spin(rpi_control)
    GPIO.cleanup()
    rpi_control.destroy_node()  
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()