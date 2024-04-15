from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="sgc_launch",
            executable="sgc_router", 
            output="screen",
            emulate_tty = True,
            parameters = [
                {"config_path": "/fog_ws/src/fogros_camp/configs/"}, 
                {"crypto_path": "/fog_ws/src/fogros_camp/configs/"}, 
                {"config_file_name": "cloudgripper.yaml"}, 
                {"whoami": "machine_user"},
        ]),
    ])