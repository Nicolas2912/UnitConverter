import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unit_converter import UnitConverter, get_conversion_explanation

class TestUnitConverter(unittest.TestCase):
    def setUp(self):
        """Set up a UnitConverter instance for each test"""
        self.converter = UnitConverter()

    # Test generic conversion functionality
    def test_invalid_quantity_type(self):
        """Test handling of invalid quantity type"""
        with self.assertRaises(ValueError):
            self.converter._convert(10, 'm', 'cm', 'invalid_type')

    def test_invalid_unit(self):
        """Test handling of invalid unit"""
        with self.assertRaises(ValueError):
            self.converter.convert_length(10, 'm', 'invalid_unit')
        with self.assertRaises(ValueError):
            self.converter.convert_length(10, 'invalid_unit', 'm')

    # Test length conversions
    def test_length_conversion(self):
        """Test various length conversions"""
        self.assertAlmostEqual(self.converter.convert_length(1, 'm', 'cm'), 100.0)
        self.assertAlmostEqual(self.converter.convert_length(1, 'km', 'm'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_length(1, 'mi', 'km'), 1.60934, places=5)
        self.assertAlmostEqual(self.converter.convert_length(3, 'ft', 'in'), 36.0)
        self.assertAlmostEqual(self.converter.convert_length(1, 'nmi', 'm'), 1852.0)
        
        # Test case insensitivity
        self.assertAlmostEqual(self.converter.convert_length(1, 'M', 'CM'), 100.0)

    # Test area conversions
    def test_area_conversion(self):
        """Test various area conversions"""
        self.assertAlmostEqual(self.converter.convert_area(1, 'm2', 'cm2'), 10000.0)
        self.assertAlmostEqual(self.converter.convert_area(1, 'km2', 'm2'), 1000000.0)
        self.assertAlmostEqual(self.converter.convert_area(1, 'ha', 'm2'), 10000.0)
        self.assertAlmostEqual(self.converter.convert_area(1, 'ac', 'm2'), 4046.86, places=2)
        
        # Test square notation alternatives
        self.assertAlmostEqual(self.converter.convert_area(1, 'sq m', 'm2'), 1.0)
        self.assertAlmostEqual(self.converter.convert_area(1, 'square km', 'km2'), 1.0)

    # Test time conversions
    def test_time_conversion(self):
        """Test various time conversions"""
        self.assertAlmostEqual(self.converter.convert_time(1, 'min', 's'), 60.0)
        self.assertAlmostEqual(self.converter.convert_time(1, 'hr', 'min'), 60.0)
        self.assertAlmostEqual(self.converter.convert_time(1, 'd', 'hr'), 24.0)
        self.assertAlmostEqual(self.converter.convert_time(1, 'wk', 'd'), 7.0)
        self.assertAlmostEqual(self.converter.convert_time(1, 'yr', 'd'), 365.0)

    # Test mass conversions
    def test_mass_conversion(self):
        """Test various mass conversions"""
        self.assertAlmostEqual(self.converter.convert_mass(1, 'kg', 'g'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_mass(1, 'g', 'mg'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_mass(1, 't', 'kg'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_mass(1, 'lb', 'kg'), 0.453592, places=6)
        self.assertAlmostEqual(self.converter.convert_mass(1, 'lb', 'oz'), 16.0, places=1)

    # Test velocity conversions
    def test_velocity_conversion(self):
        """Test various velocity conversions"""
        self.assertAlmostEqual(self.converter.convert_velocity(1, 'm/s', 'km/h'), 3.6)
        self.assertAlmostEqual(self.converter.convert_velocity(1, 'km/h', 'm/s'), 0.277778, places=6)
        self.assertAlmostEqual(self.converter.convert_velocity(1, 'mph', 'km/h'), 1.60934, places=5)
        self.assertAlmostEqual(self.converter.convert_velocity(1, 'kn', 'm/s'), 0.514444, places=6)

    # Test volume conversions
    def test_volume_conversion(self):
        """Test various volume conversions"""
        self.assertAlmostEqual(self.converter.convert_volume(1, 'l', 'ml'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_volume(1, 'gal', 'l'), 3.78541, places=5)
        self.assertAlmostEqual(self.converter.convert_volume(1, 'm3', 'l'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_volume(1, 'cup', 'ml'), 240.0)
        
        # Test aliases
        self.assertAlmostEqual(self.converter.convert_volume(1, 'liter', 'milliliter'), 1000.0)
        self.assertAlmostEqual(self.converter.convert_volume(1, 'gallon', 'l'), 3.78541, places=5)

    # Test data conversions
    def test_data_conversion(self):
        """Test various data storage conversions"""
        self.assertAlmostEqual(self.converter.convert_data(1, 'kb', 'byte'), 1024.0)
        self.assertAlmostEqual(self.converter.convert_data(1, 'mb', 'kb'), 1024.0)
        self.assertAlmostEqual(self.converter.convert_data(1, 'gb', 'mb'), 1024.0)
        self.assertAlmostEqual(self.converter.convert_data(1, 'byte', 'bit'), 8.0)
        
        # Test aliases
        self.assertAlmostEqual(self.converter.convert_data(1, 'kilobyte', 'byte'), 1024.0)
        self.assertAlmostEqual(self.converter.convert_data(1, 'megabyte', 'kilobyte'), 1024.0)

    # Test acceleration conversions
    def test_acceleration_conversion(self):
        """Test various acceleration conversions"""
        self.assertAlmostEqual(self.converter.convert_acceleration(1, 'm/s2', 'g'), 0.101972, places=6)
        self.assertAlmostEqual(self.converter.convert_acceleration(1, 'g', 'm/s2'), 9.80665)
        self.assertAlmostEqual(self.converter.convert_acceleration(1, 'ft/s2', 'm/s2'), 0.3048, places=4)
        
        # Test aliases
        self.assertAlmostEqual(self.converter.convert_acceleration(1, 'mps2', 'g'), 0.101972, places=6)

    # Test temperature conversions
    def test_temperature_conversion(self):
        """Test various temperature conversions"""
        # Celsius to Fahrenheit
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'C', 'F'), 32.0)
        self.assertAlmostEqual(self.converter.convert_temperature(100, 'C', 'F'), 212.0)
        
        # Celsius to Kelvin
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'C', 'K'), 273.15)
        
        # Fahrenheit to Celsius
        self.assertAlmostEqual(self.converter.convert_temperature(32, 'F', 'C'), 0.0)
        self.assertAlmostEqual(self.converter.convert_temperature(212, 'F', 'C'), 100.0)
        
        # Kelvin to Celsius
        self.assertAlmostEqual(self.converter.convert_temperature(273.15, 'K', 'C'), 0.0)
        
        # Fahrenheit to Kelvin
        self.assertAlmostEqual(self.converter.convert_temperature(32, 'F', 'K'), 273.15)
        
        # Same unit (no conversion)
        self.assertAlmostEqual(self.converter.convert_temperature(100, 'C', 'C'), 100.0)
        
        # Test with full unit names
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'Celsius', 'Fahrenheit'), 32.0)
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'Celsius', 'Kelvin'), 273.15)
        
        # Test invalid temperature unit
        with self.assertRaises(ValueError):
            self.converter.convert_temperature(0, 'C', 'invalid_unit')

    # Test explanation function
    def test_conversion_explanation(self):
        """Test the explanation generation function"""
        # Temperature explanations
        self.assertIn("°F = (°C × 9/5) + 32", 
                      get_conversion_explanation("Temperature", "Celsius", "Fahrenheit", 20, 68))
        
        self.assertIn("°C = (°F - 32) × 5/9", 
                      get_conversion_explanation("Temperature", "Fahrenheit", "Celsius", 68, 20))
        
        self.assertIn("K = °C + 273.15", 
                      get_conversion_explanation("Temperature", "Celsius", "Kelvin", 0, 273.15))
        
        # Factor explanations
        self.assertIn("Multiply by", 
                      get_conversion_explanation("Length", "m", "cm", 1, 100))
        
        self.assertIn("Multiply by", 
                      get_conversion_explanation("Length", "km", "m", 1, 1000))
        
        self.assertIn("Divide by", 
                      get_conversion_explanation("Length", "cm", "m", 100, 1))
        
        # Same unit
        self.assertIn("Units are equivalent", 
                      get_conversion_explanation("Length", "m", "m", 10, 10))
        
        # Zero input
        self.assertIn("input was zero", 
                      get_conversion_explanation("Length", "m", "cm", 0, 0))


class TestUnitConverterEdgeCases(unittest.TestCase):
    def setUp(self):
        """Set up a UnitConverter instance for each test"""
        self.converter = UnitConverter()

    def test_zero_values(self):
        """Test conversions with zero values"""
        self.assertEqual(self.converter.convert_length(0, 'm', 'km'), 0.0)
        self.assertEqual(self.converter.convert_area(0, 'm2', 'ha'), 0.0)
        self.assertEqual(self.converter.convert_temperature(0, 'C', 'F'), 32.0)  # Exception: temperature offsets
        self.assertEqual(self.converter.convert_temperature(0, 'K', 'C'), -273.15)  # Exception: temperature offsets

    def test_negative_values(self):
        """Test conversions with negative values"""
        self.assertAlmostEqual(self.converter.convert_length(-5, 'm', 'cm'), -500.0)
        self.assertAlmostEqual(self.converter.convert_mass(-10, 'kg', 'g'), -10000.0)
        self.assertAlmostEqual(self.converter.convert_temperature(-40, 'C', 'F'), -40.0)  # Special case: -40°C = -40°F

    def test_large_values(self):
        """Test conversions with very large values"""
        large_value = 1e12  # 1 trillion
        self.assertAlmostEqual(self.converter.convert_length(large_value, 'm', 'km'), large_value / 1000.0)
        self.assertAlmostEqual(self.converter.convert_data(large_value, 'byte', 'tb'), large_value / (1024.0**4))

    def test_small_values(self):
        """Test conversions with very small values"""
        small_value = 1e-12  # 1 trillionth
        self.assertAlmostEqual(self.converter.convert_length(small_value, 'km', 'm'), small_value * 1000.0)
        self.assertAlmostEqual(self.converter.convert_mass(small_value, 'g', 'kg'), small_value / 1000.0)

    def test_case_insensitivity(self):
        """Test that unit names are case-insensitive"""
        self.assertAlmostEqual(self.converter.convert_length(1, 'M', 'CM'), 100.0)
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'c', 'f'), 32.0)
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'C', 'F'), 32.0)
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'celsius', 'FAHRENHEIT'), 32.0)

    def test_bidirectional_conversion(self):
        """Test that conversions work correctly in both directions"""
        # Forward
        celsius_to_fahrenheit = self.converter.convert_temperature(25, 'C', 'F')
        # Backward
        fahrenheit_to_celsius = self.converter.convert_temperature(celsius_to_fahrenheit, 'F', 'C')
        # Should get back original value (approximately)
        self.assertAlmostEqual(fahrenheit_to_celsius, 25.0, places=10)
        
        # Same for other types
        meters_to_feet = self.converter.convert_length(10, 'm', 'ft')
        feet_to_meters = self.converter.convert_length(meters_to_feet, 'ft', 'm')
        self.assertAlmostEqual(feet_to_meters, 10.0, places=10)


if __name__ == '__main__':
    unittest.main() 