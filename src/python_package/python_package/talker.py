import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__("talker_node")
        self.publisher = self.create_publisher(String, "greeting", 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.declare_parameter("sentence", "Hello everyone!")

    def timer_callback(self):
        msg = String()
        msg.data = self.get_parameter("sentence").get_parameter_value().string_value
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args=None):

    rclpy.init(args=args)
    publisher = Talker()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()