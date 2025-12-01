import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):

    def __init__(self):
        super().__init__("listener_py")
        self.subscriber = self.create_subscription(String, "greeting", self.listener_callback, 10)
        self.subscriber

    def listener_callback(self, msg):
        self.get_logger().info("Hearing: '%s'" % msg.data)


def main(args=None):

    rclpy.init(args=args)
    subscriber = Listener()
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":

    main()

