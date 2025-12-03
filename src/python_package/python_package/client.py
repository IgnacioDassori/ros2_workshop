import rclpy
from rclpy.node import Node

from interfaces_pkg.srv import GetPoseDistance
from interfaces_pkg.msg import Pose3D
from nav_msgs.msg import Odometry

class SimpleClient(Node):
    def __init__(self):
        super().__init__("simple_client")

        self.cli = self.create_client(GetPoseDistance, "get_distance")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.odom_sub = self.create_subscription(Odometry, "odom", self.odom_callback, 10)
        self.taget_sub = self.create_subscription(Pose3D, "target", self.target_callback, 10)

        self.latest_odom = None
        self.latest_target = None

        self.timer = self.create_timer(1.0, self.timer_callback)

    def odom_callback(self, msg):
        self.latest_odom = msg

    def target_callback(self, msg):
        self.latest_target = msg

    def timer_callback(self):
        if self.latest_odom is None or self.latest_target is None:
            return
        
        req = GetPoseDistance.Request()
        req.base_odom = self.latest_odom
        req.target_pose = self.latest_target

        future = self.cli.call_async(req)
        future.add_done_callback(self.handle_response)

    def handle_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Distance to target is {response.dist}")
        except Exception as e:
            self.get_logger().info(f"Service failed: {e}")
            
        self.latest_target = None


def main(args=None):

    rclpy.init(args=args)
    client = SimpleClient()
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":

    main()
