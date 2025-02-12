import unittest
from app.simulation import simulate_energy_consumption
from app.models import Building

class SimulationTestCase(unittest.TestCase):
    def test_simulate_energy_consumption(self):
        building = Building(name="Test Building", area=100.0, materials="Brick", windows=5,
                            orientation="South", insulation="Good", hvac="Central")
        result = simulate_energy_consumption(building)
        self.assertIn('total_energy_consumption', result)
        self.assertIn('thermal_losses', result)
        self.assertIn('solar_gains', result)

if __name__ == '__main__':
    unittest.main()