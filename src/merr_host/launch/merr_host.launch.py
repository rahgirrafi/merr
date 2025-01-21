# I am najeeb, the novice engineer. And I created a branch yay!
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


ARGUMENTS = [
    # DeclareLaunchArgument('namespace', default_value='',
    #                       description='Robot namespace'),
    # DeclareLaunchArgument('rviz', default_value='false',
    #                       choices=['true', 'false'], description='Start rviz.'),
    # DeclareLaunchArgument('world', default_value='warehouse',
    #                       description='Ignition World'),
    # DeclareLaunchArgument('model', default_value='standard',
    #                       choices=['standard', 'lite'],
    #                       description='Turtlebot4 Model'),
]

# for pose_element in ['x', 'y', 'z', 'yaw']:
#     ARGUMENTS.append(DeclareLaunchArgument(pose_element, default_value='0.0',
#                      description=f'{pose_element} component of the robot pose.'))


def generate_launch_description():
    # # Directories
    # pkg_turtlebot4_ignition_bringup = get_package_share_directory(
    #     'turtlebot4_ignition_bringup')

    # # Paths
    # ignition_launch = PathJoinSubstitution(
    #     [pkg_turtlebot4_ignition_bringup, 'launch', 'ignition.launch.py'])
    # robot_spawn_launch = PathJoinSubstitution(
    #     [pkg_turtlebot4_ignition_bringup, 'launch', 'turtlebot4_spawn.launch.py'])

    # ignition = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([ignition_launch]),
    #     launch_arguments=[
    #         ('world', LaunchConfiguration('world'))
    #     ]
    # )

    # robot_spawn = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([robot_spawn_launch]),
    #     launch_arguments=[
    #         ('namespace', LaunchConfiguration('namespace')),
    #         ('rviz', LaunchConfiguration('rviz')),
    #         ('x', LaunchConfiguration('x')),
    #         ('y', LaunchConfiguration('y')),
    #         ('z', LaunchConfiguration('z')),
    #         ('yaw', LaunchConfiguration('yaw'))]
    # )

    camera_capture_node = Node(package='v4l2_camera', executable='v4l2_camera_node', output='screen'
                        name='v4l2_camera_node',
                        output='screen',
                        )
    

    # # Create launch description and add actions
    ld = LaunchDescription(ARGUMENTS)
    # ld.add_action(ignition)
    ld.add_action(camera_capture_node)

    return ld