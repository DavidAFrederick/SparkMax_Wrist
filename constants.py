import math
from enum import Enum

# CAN IDS
DT_LEFT_LEADER = 1
DT_RIGHT_LEADER = 2
DT_LEFT_FOLLOWER = 3
DT_RIGHT_FOLLOWER = 4
ELEVATOR = 6
INTAKE_MOTOR = 7
WRIST_MOTOR = 8
WRIST_MOTOR_REV = 8
ClIMBER_NOTOR = 9

# ROBORIO Ports

# DIO
WRIST_ANGLE_ENCODER = 0

# Default Robot loop period
ROBOT_PERIOD_MS = 0.020  # 50Hz, or 20 times a second

# Controller Mapping information
CONTROLLER_DRIVER_PORT = 0
CONTROLLER_PARTNER_PORT = 1
CONTROLLER_FORWARD_REAL = 1
CONTROLLER_FORWARD_SIM = 1
CONTROLLER_TURN_REAL = 4
CONTROLLER_TURN_SIM = 0

