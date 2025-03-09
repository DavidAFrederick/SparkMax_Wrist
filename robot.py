#!/usr/bin/env python3

#   WHEN YOU GET AN FATAL ERROR RUN: 
#   py -3 -m robotpy installer niweb disable

import wpilib
from wpilib import RobotBase, DriverStation
from commands2 import (
    TimedCommandRobot,
    CommandScheduler,
    Command,
    PrintCommand,
    RunCommand,
    WaitCommand,
    cmd,
)
from commands2.button import CommandXboxController, Trigger, JoystickButton, POVButton
from wpimath.geometry import Pose2d
from wrist import (
        SetWristAngleAuto,
        WristControl, 
        Set_Wrist_Angle_manual_and_auto_with_PID,
        Set_Global_Wrist_Angle,
        SetWrist_Manual
)
import constants

class MyRobot(TimedCommandRobot):
    """Class that defines the totality of our Robot"""

    def robotInit(self) -> None:
        # Setup the operator interface (typically CommandXboxController)
        # self._driver_controller = CommandXboxController(
        #     constants.CONTROLLER_DRIVER_PORT        )
        self._partner_controller = CommandXboxController(
            constants.CONTROLLER_PARTNER_PORT
        )

        self._wrist: WristControl = WristControl()
        wpilib.SmartDashboard.putData("Wrist", self._wrist)

        self.__configure_button_bindings()

        self._auto_command = None
        self._current_pose = Pose2d()

    def __configure_button_bindings(self) -> None:


        ######################## Partner controller controls #########################
        #  Third parameter is False so the command does not end.
        # self._wrist.setDefaultCommand(Set_Wrist_Angle_manual_and_auto_with_PID(self._wrist, self._partner_controller, False))
        self._wrist.setDefaultCommand(SetWrist_Manual(self._wrist, self._partner_controller))


        # self._driver_controller.a().onTrue(Set_Global_Wrist_Angle(self._wrist, 0))  # Example target angle
        # self._driver_controller.b().onTrue(Set_Global_Wrist_Angle(self._wrist, 20))  # Example target angle
        # self._driver_controller.x().onTrue(Set_Global_Wrist_Angle(self._wrist, 45))  # Example target angle
        # self._driver_controller.y().onTrue(Set_Global_Wrist_Angle(self._wrist, 60))  # Example target angle


        # self._driver_controller.a().whileTrue(Set_Global_Wrist_Angle(self._wrist, 0))  # Example target angle
        # self._driver_controller.b().whileTrue(Set_Global_Wrist_Angle(self._wrist, 20))  # Example target angle
        # self._driver_controller.x().whileTrue(Set_Global_Wrist_Angle(self._wrist, 45))  # Example target angle
        # self._driver_controller.y().whileTrue(Set_Global_Wrist_Angle(self._wrist, 60))  # Example target angle

        # self._wrist.setDefaultCommand(SetWrist_Manual(self._wrist, self._partner_controller))

        # self._driver_controller.a().whileTrue(Set_Wrist_Angle_with_PID(self._wrist, 0))  # Example target angle
        # self._driver_controller.b().whileTrue(Set_Wrist_Angle_with_PID(self._wrist, 20))  # Example target angle
        # self._driver_controller.x().whileTrue(Set_Wrist_Angle_with_PID(self._wrist, 45))  # Example target angle
        # self._driver_controller.y().whileTrue(Set_Wrist_Angle_with_PID(self._wrist, 60))  # Example target angle


    def getAutonomousCommand(self) -> Command:
        return self._auto_chooser.getSelected()

    def teleopInit(self) -> None:
        if self._auto_command is not None:
            self._auto_command.cancel()

    def testInit(self) -> None:
        CommandScheduler.getInstance().cancelAll()

    def autonomousInit(self) -> None:
        # If we're starting on the blue side, offset the Navx angle by 180
        # so 0 degrees points to the right for NWU
        self._drivetrain.set_alliance_offset()
        self._drivetrain.reset_encoders()

        # Set the proper April Tag ID target
        # self._vision.set_target_tag(ShooterPosition.SUBWOOFER_2)
        self._auto_command = self.getAutonomousCommand()

        if self._auto_command is not None:
            self._auto_command.schedule()

    def disabledPeriodic(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def testPeriodic(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        return super().teleopPeriodic()
