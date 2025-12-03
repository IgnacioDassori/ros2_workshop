import rclpy
import math
from rclpy.node import Node

from interfaces_pkg.srv import GetPoseDistance

class SimpleService(Node):
    def __init__(self):
        super().__init__("simple_server")
        self.srv = self.create_service(GetPoseDistance, "get_distance", self.service_callback)

    def service_callback(self, request, response):
        x_odom = request.base_odom.pose.pose.position.x
        y_odom = request.base_odom.pose.pose.position.y
        z_odom = request.base_odom.pose.pose.position.z
        x_target = request.target_pose.position.x
        y_target = request.target_pose.position.y
        z_target = request.target_pose.position.z
        response.dist = math.sqrt(
            (x_odom - x_target)**2 +
            (y_odom - y_target)**2 +
            (z_odom - z_target)**2
        )
        return response
    

def main(args=None):

    rclpy.init(args=args)
    service = SimpleService()
    rclpy.spin(service)
    service.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":

    main()