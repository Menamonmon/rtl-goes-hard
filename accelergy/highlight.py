import os
from accelergy.plug_in_interface.estimator import (
    Estimator, actionDynamicEnergy, add_estimator_path, remove_estimator_path
)
class HighLight(Estimator):
    name = "HighLight"  # This must match the `subclass` or identification logic

    @classmethod
    def is_compatible(cls, class_name, attributes):
        return (
            class_name == "storage"
            and "WORD_SIZE" in attributes
        )
    percent_accuracy_0_to_100 = 69

    def __init__(self, WORD_SIZE: int = 8):
        super().__init__()  # <- Important to set up the logger
        self.logger.info(
            "The __init__ function is called if the name and "
            "required arguments match."
        )
        assert WORD_SIZE > 0, "Arguments must be positive integers."
        self.word_size = WORD_SIZE
        
    @actionDynamicEnergy
    def compute(self, global_cycle_seconds: float, action_latency_cycles: int) -> float:
        self.logger.info("@actionDynamicEnergy can decorate any number of actions.")
        power_per_bit_uw = 24.1  # Power per bit in microwatts

        total_power_uw = self.word_size * power_per_bit_uw
        total_energy_j = total_power_uw * global_cycle_seconds * 10**(-6) # Calculate energy in joules

        return total_energy_j



    def get_area(self) -> float:
        self.logger.info("The get_area function is required.")
        #area from RTL simulation for word_size=8 is 111247 um^2, and it scales linearly with number of bits, therefore 111247/6=13905um2 area per bit
        area_sim_per_bit_um = 13905 
        total_bits = self.word_size
        total_area_um2 = total_bits * area_sim_per_bit_um
        return total_area_um2*10**(-12) #Area in m2

    def leak(self, global_cycle_seconds: float) -> float:
        power_per_bit_uw = 0.344  # Power per bit in microwatts

        total_power_uw = self.word_size * power_per_bit_uw
        total_energy_j = total_power_uw * global_cycle_seconds * 10**(-6)   # Calculate energy in joules

        return total_energy_j

    @staticmethod
    def quick_install_this_file():
        add_estimator_path(os.path.abspath(__file__))

    @staticmethod
    def quick_uninstall_this_file():
        remove_estimator_path(os.path.abspath(__file__))
        
