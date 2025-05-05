import os
from accelergy.plug_in_interface.estimator import (
    Estimator, actionDynamicEnergy, add_estimator_path, remove_estimator_path
)
class Nvidia(Estimator):
    name = "Nvidia"  # This must match the `subclass` or identification logic

    @classmethod
    def is_compatible(cls, class_name, attributes):
        return (
            class_name == "storage"
            and "BLOCK_SIZE" in attributes
            and "NUM_SELECT" in attributes
            and "WORD_SIZE" in attributes
        )
    percent_accuracy_0_to_100 = 50

    def __init__(self, BLOCK_SIZE: int, NUM_SELECT: int = 5, WORD_SIZE: int = 32):
        super().__init__()  # <- Important to set up the logger
        self.logger.info(
            "The __init__ function is called if the name and "
            "required arguments match."
        )
        assert BLOCK_SIZE > 0 and NUM_SELECT > 0 and WORD_SIZE > 0, "Arguments must be positive integers."
        self.block_size = BLOCK_SIZE
        self.num_select = NUM_SELECT
        self.word_size = WORD_SIZE
        
    @actionDynamicEnergy
    def compute(self, global_cycle_seconds: float, action_latency_cycles: int) -> float:
        self.logger.info("@actionDynamicEnergy can decorate any number of actions.")
        power_per_bit_uw = 2.57  #  Power per bit in microwatts 247/(4*3*8)

        total_bits = self.block_size * self.num_select * self.word_size
        total_power_uw = total_bits * power_per_bit_uw
        total_energy_j = total_power_uw * global_cycle_seconds*10**(-6)  # Convert picojoules to joules

        return total_energy_j
    def get_area(self) -> float:
        self.logger.info("The get_area function is required.")
        area_sim_per_bit_um = 4654.2 #area from RTL simulation for num_select=3, word_size=8: 111701/(3*8)
        total_bits = self.num_select * self.word_size
        total_area_um2 = total_bits * area_sim_per_bit_um
        total_area_m2 = total_area_um2*10**(-12)  # Convert um² to m²

        return total_area_m2

    def leak(self, global_cycle_seconds: float) -> float:
        self.logger.info("The leak function is required.")
        leakage_power_w = 3.4382011904199317E-7  # Leakage power in watts
        return leakage_power_w * global_cycle_seconds

    @staticmethod
    def quick_install_this_file():
        add_estimator_path(os.path.abspath(__file__))

    @staticmethod
    def quick_uninstall_this_file():
        remove_estimator_path(os.path.abspath(__file__))
        