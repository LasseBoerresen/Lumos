from dynamixel_adapter import DynamixelAdapter
from motor_state import MotorState


class DxlMotor:
    def __init__(self, id, adapter: DynamixelAdapter, state: MotorState, drive_mode):
        self.id = id
        self.adapter = adapter
        self.state = state
        self.drive_mode = drive_mode

        self.adapter.init_single(self.id, self.drive_mode)

    @property
    def state(self):
        self.state = self.adapter.read_state(self.id)
        return self.__state

    @state.setter
    def state(self, state_new):
        self.__state = state_new

    def set_goal_position(self, position):
        self.adapter.write_goal_pos(self.id, position)
