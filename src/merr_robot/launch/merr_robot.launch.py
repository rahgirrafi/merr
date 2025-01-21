from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():
  
    camera_capture_node = Node(
        package='v4l2_camera', 
        executable='v4l2_camera_node', 
        output='screen',
        name='front_camera',
        parameters=[{
            'device': '/dev/video0',
            'frame_id': 'camera',
            'width': 640,
            'height': 480,
            'framerate': 30,
        }],


    rplidar_node = Node(
            name='rplidar_composition',
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 115200,  # A1
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity',
            }],
        )
    

    

    # # Create launch description and add actions
    ld = LaunchDescription()
    # ld.add_action(ignition)
    ld.add_action(camera_capture_node)
    ld.add_action(rplidar_node)

    return ld