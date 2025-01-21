
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    rviz = Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', ['/home/host/merr_ws/src/merr_host/rviz/merr_host.rviz']],
        )
    

    image_transport = Node(
            package='image_transport', 
            executable='republish', 
            output='screen',
            parameters=[{'in_transport': 'compressed', 'out_transport': 'raw'}],
            remappings=[
                ('in/compressed', '/image_raw/compressed'),
                ('out', '/image_raw/uncompressed')
            ],
        )

    ld = LaunchDescription()
    ld.add_action(rviz)
    ld.add_action(image_transport)

    return ld