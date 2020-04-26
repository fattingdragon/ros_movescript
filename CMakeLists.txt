cmake_minimum_required(VERSION 2.8.3)
project(test_py)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  test.msg
)

generate_messages(
  DEPENDENCIES
  test_py
)
#对于C++结点的CMakeLists.txt文件，INCLUDE_DIRS include和LIBRARIES test_py不能注释，
#但是对于python,这两行不注释，catkin_make通不过
catkin_package(
#INCLUDE_DIRS include
#LIBRARIES test_py
CATKIN_DEPENDS rospy message_runtime
DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

