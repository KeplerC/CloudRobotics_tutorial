from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_name', 
            default_value='1',
            description='Cloudgripper robot name'
        ),
        Node(
            package="sgc_launch",
            executable="sgc_router", 
            output="screen",
            emulate_tty = True,
            parameters = [
                {"config_file_path": "/fog_ws/src/fogros_camp/configs/"}, 
                {"config_file_name": "cloudgripper.yaml"}, 
                {"whoami": "cloud"},
        ]),
        Node(
            package='cloudgripper_ros',
            executable='robot_subscriber',
            name='robot_subscriber',
            parameters=[{'robot_name': LaunchConfiguration('robot_name')}]
        ),
        Node(
            package='cloudgripper_ros',
            executable='image_publisher',
            name='image_publisher',
            parameters=[{'robot_name': LaunchConfiguration('robot_name')}]
        ),
        Node(
            package='cloudgripper_ros',
            executable='state_publisher',
            name='state_publisher',
            parameters=[{'robot_name': LaunchConfiguration('robot_name')}]
        ),
    ])