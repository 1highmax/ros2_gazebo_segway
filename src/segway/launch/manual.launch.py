#!/usr/bin/python3
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable 

import sys


share_dir = get_package_share_directory('segway')
gzenv = {'GAZEBO_MODEL_PATH': share_dir + '/gzmodels//robots',
         'GAZEBO_MASTER_URI': "127.0.0.1:11345",
         'GAZEBO_IP': "127.0.0.1"}

def generate_launch_description():
    return launch.LaunchDescription([

        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
            description='Prefix for node names'),

        ExecuteProcess(
            cmd=['gzclient', '--verbose'],
            output='screen',
            additional_env=gzenv,
            ),

        ExecuteProcess(
            cmd=['ros2', 'run', 'gazebo_ros', 'spawn_entity.py', '-entity', 'segway_model', '-z 0', '-x 0', '-y 0', '-R 0', '-P 0', '-Y 0', '-file', share_dir + '/gzmodels/segway/model.sdf'],
            # output='screen',
            additional_env=gzenv,
            ),

        launch_ros.actions.Node(
            package='joy',
            executable='joy_node',
            output='screen',
            emulate_tty=True,
            parameters=[
            ],
            remappings=[
            ],
            arguments=['--ros-args', '--log-level', 'error']
        ),

        launch_ros.actions.Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {"axis_linear.x": 1},
                {"scale_linear.x": 2.0},
            ],
            remappings=[
            ],
            arguments=['--ros-args', '--log-level', 'error']
        ),

    ])


def main(argv=sys.argv[1:]):
    ld = generate_launch_description()
    ls = launch.LaunchService(argv=argv, debug=False)
    ls.include_launch_description(ld)
    ls.run()
    
if __name__ == "__main__":
    main()

    
