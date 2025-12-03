from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    tb3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')

    empty_world_launch = os.path.join(tb3_gazebo_dir, 'launch', 'empty_world.launch.py')

    service_node = Node(
        package='python_package',
        executable='service',
        name='simple_service'
    )

    client_node = Node(
        package='python_package',
        executable='client',
        name='simple_client'
    )

    return LaunchDescription([
        SetEnvironmentVariable('TURTLEBOT3_MODEL', 'burger'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(empty_world_launch)
        ),
        service_node,
        client_node
    ])
