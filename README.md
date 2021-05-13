# A ros2 workspace with a self balancing segway gazebo plugin

The purpose of this repo is:
- To be a template for developing ros2 gazebo extensions in vscode
- To facilitate the setup of gzserver/gzclient, ros2 launch, gdb, sdf files, shared libraries, cmake files and everything else that is needed for ros2 gazebo development in vscode
- To be a playground for modifications of the plugin

- vscode folder
  - launch.json - launch debug configurations for developing the plugin
  - tasks.json - tasks for the debug configuration

- ros2 workspace
  - ros2 package "segway"
    - launch - a launch file to run joystick and gzclient 
    - src - source file for the plugin
    - gzmodels - gazebo files
        - world
        - model

## How to use:
- ctrl shift p 
- select and start debugging
- container/loader

## Troubleshooting:
Necessary env settings for ros2 gazebo development:
```
source /opt/ros/foxy/setup.bash
source ~/segway/install/setup.bash
export GAZEBO_RESOURCE_PATH=/usr/share/gazebo-11/media:/usr/share/gazebo-11/models:/usr/share/gazebo-11/worlds:/usr/share/gazebo-11:${GAZEBO_RESOURCE_PATH}
```