cmake_minimum_required(VERSION 3.5)
project(segway)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(tf2_ros REQUIRED)

# add_executable(plugin src/plugin.cpp)
# target_include_directories(plugin PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)
# ament_target_dependencies(
#   plugin
#   "rclcpp"
#   "std_msgs"
#   "sensor_msgs"
#   "nav_msgs"
#   "gazebo_ros"
# )

# install(TARGETS plugin
#   DESTINATION lib/${PROJECT_NAME})

# gazebo_ros_segway_drive
add_library(gazebo_ros_segway_drive SHARED
  src/gazebo_ros_segway.cpp
)
target_include_directories(gazebo_ros_segway_drive PUBLIC include)
ament_target_dependencies(gazebo_ros_segway_drive
  "gazebo_ros"
  "geometry_msgs"
  "nav_msgs"
  "rclcpp"
  "sensor_msgs"
  "tf2"
  "tf2_geometry_msgs"
  "tf2_ros"
)
ament_export_libraries(gazebo_ros_segway_drive)
if(ENABLE_PROFILER)
  target_include_directories(gazebo_ros_segway_drive PUBLIC ${ignition-common3_INCLUDE_DIRS})
  target_link_libraries(gazebo_ros_segway_drive ${ignition-common3_LIBRARIES})
endif()

install(DIRECTORY
  gzmodels
  DESTINATION share/${PROJECT_NAME}/
)
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)
install(TARGETS gazebo_ros_segway_drive
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
