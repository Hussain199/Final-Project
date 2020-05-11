# Final-Project

# ROS package: |Hussain_topics|

|Hussain_topics is a ROS package that includes five codes and each has its job. First is the topic_publisher, it publish the count to the counter using the publish method, it increment the count, and wait until the sleep method to iterate. Second is the topic_subscribe, it subscribes to the counter, and direct messages, then repeat. Also , we have two more things message-publisher and message-subscriber, which take thing to a complex level. Finaly, there was a doubler file which take the published and double it then send it to the subscriber. This can be used as a comunication method between real live and robots when they are moving, they will need a guidens where to go without hitting any thing so it'll send a signle and get one back and know the bath it needs to to take from the data.|

## Requirements

|It will run on ros melodic using Ubuntu.|

## Installation and configuration

|Using catkin_create_pkg Hussain_topics\rospy std_msgs message_runtime message_generation, we can create the package, then using the touch command to create the file, then using chmod u+x we make the file executable, then we open it using any text editer in this case was sublime, to put the code we need. Then after sorcing our files. Finaly using git add -A, git commit -m, and git push, we send our work to the GitHub repository.|

## Getting started

|We can use roscore to start.|

## Usage

| Using rosrun we can test our work.|


# ROS package: |Hussain_services|

|Hussain_services is a ROS package that includes two codes and each has its job. First is the service_server, it imports the service, wait for service, set up a proxy server for communication, use the service. Second is the service_client, which prints and shows whats is going on the server. This can count how many words were written in this case. However, in general it gets a sensor value, sets a parameter, or performe a computation.|

## Requirements

|It will run on ros melodic using Ubuntu.|

## Installation and configuration

|Using catkin_create_pkg Hussain_services\roscpp rospy message_generation message_runtime, we can create the package, then using the touch command to create the files, then using chmod u+x we make the files executable, then we open them using any text editer in this case was sublime, to put the code we need. Then after sorcing our files. Finaly using git add -A, git commit -m, and git push, we send our work to the GitHub repository.|

## Getting started

|We can use roscore to start.|

## Usage

|Using rosrun we can test our work.|


# ROS package: |Hussain_actions|

|Hussain_actions is a ROS package that includes two codes and each has its job. First is the fancy_action_server, it check on the client request for errors, check  for  client  request  to  preemptively  abort  goal  andabort with result if necessary, set and publish feedback, when goal is met, publish the result, register the action, and start the action and wait for requests. Second is the fancy_action_client, it import the Python package action lib, import the action’s generated message types, define a feedback callback function, register an action client and wait for server connection, define and send goal to server, wait for results, and do what you like with them. This can be used to navigating to a location, performe a complex manipulation, or performe a long calculation.|

## Requirements

|It will run on ros melodic using Ubuntu.|

## Installation and configuration

|Using catkin_create_pkg Hussain_actionsroscpp rospy actionlib_msgs, we can create the package, then using the touch command to create the files, then using chmod u+x we make the files executable, then we open them using any text editer in this case was sublime, to put the code we need. Then after sorcing our files. Finaly using git add -A, git commit -m, and git push, we ssend our work to the GitHub repository.|

## Getting started

|We can use roscore to start.|

## Usage

|Using rosrlaunch we can test our work.|
