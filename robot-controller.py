import URBasic
import time
import math



ROBOT_IP = '192.168.186.135'
ACCELERATION = 0.4  # Robot acceleration value
VELOCITY = 0.4  # Robot speed value


# initialise robot with URBasic
print("initialising robot")
robotModel = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=ROBOT_IP,robotModel=robotModel)

robot.reset_error()
print("robot initialised")
time.sleep(1)


# The Joint position the robot starts at
robot_startposition = (math.radians(11),
                    math.radians(-92),
                    math.radians(-92),
                    math.radians(-82),
                    math.radians(90),
                    math.radians(157))

# Move Robot to the midpoint of the lookplane
robot.movej(q=robot_startposition, a=ACCELERATION, v=VELOCITY)

robot.init_realtime_control()  # starts the realtime control loop on the Universal-Robot Controller
time.sleep(1) # just a short wait to make sure everything is initialised

robot.init_realtime_control()  # starts the realtime control loop on the Universal-Robot Controller
time.sleep(10) # just a short wait to make sure everything is initialised


# Parameters for the circle
radius = 0.1  # Radius of the circle
center = robot.get_actual_tcp_pose()  # Center of the circle is the current position
circle_points = 100  # Number of points to generate along the circle

# Calculate the points along the circle
for i in range(circle_points):
    # Calculate the angle in radians
    angle = 2 * math.pi * (i / circle_points)

    # Calculate the new position
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    z = center[2]

    # Create the target pose
    target_pose = [x, y, z, center[3], center[4], center[5]]

    # Move the robot to the target pose
    robot.movel(pose=target_pose, a=ACCELERATION, v=VELOCITY)

    # robot.set_realtime_pose(target_pose)
    # time.sleep(1)

# Return to the center
#robot.movel(pose=center, a=ACCELERATION, v=VELOCITY)

