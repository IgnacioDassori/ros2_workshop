from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='python_package',
            namespace='convo_1',
            executable='talker',
            name='talker_1',
            parameters=[
                {"sentence": "How are you doing?"}
            ]
        ),
        Node(
            package='cpp_package',
            namespace='convo_1',
            executable='listener',
            name='listener_1'
        ),
        Node(
            package='python_package',
            namespace='convo_2',
            executable='talker',
            name='talker_2',
            parameters=[
                {"sentence": "Have a good night."}
            ]
        ),
        Node(
            package='cpp_package',
            namespace='convo_2',
            executable='listener',
            name='listener_2'
        )
    ])