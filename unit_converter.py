class UnitConverter:
    """
    A class to perform conversions between various units for different physical quantities.
    """

    def __init__(self):
        # Conversion factors relative to a base unit
        # Base units: meter (m), square meter (m^2), second (s), kilogram (kg), meter/second (m/s)
        self._factors = {
            'length': {
                'm': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001,
                'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254,
                'nmi': 1852.0 # Nautical mile
            },
            'area': {
                'm2': 1.0, 'km2': 1_000_000.0, 'cm2': 0.0001, 'mm2': 0.000001,
                'ha': 10000.0, 'ac': 4046.86,
                'mi2': 2_589_988.11, 'yd2': 0.836127, 'ft2': 0.092903, 'in2': 0.00064516
            },
            'time': {
                's': 1.0, 'ms': 0.001, 'min': 60.0, 'hr': 3600.0,
                'd': 86400.0, 'wk': 604800.0, 'yr': 31_536_000.0 # Approximate year (365 days)
            },
            'mass': {
                'kg': 1.0, 'g': 0.001, 'mg': 0.000001, 't': 1000.0, # metric ton
                'lb': 0.453592, 'oz': 0.0283495
            },
            'velocity': {
                'm/s': 1.0, 'km/h': 1 / 3.6, 'mph': 0.44704,
                'ft/s': 0.3048, 'kn': 0.514444 # knot
            },
            # New conversion types
            'volume': {
                'l': 1.0, 'ml': 0.001, 'cl': 0.01, 'dl': 0.1, 
                'm3': 1000.0, 'cm3': 0.001, 'mm3': 0.000001,
                'gal': 3.78541, 'qt': 0.946353, 'pt': 0.473176, 'fl oz': 0.0295735,
                'cup': 0.24, 'tbsp': 0.0147868, 'tsp': 0.00492892
            },
            'data': {
                'byte': 1.0, 'kb': 1024.0, 'mb': 1024.0 * 1024.0,
                'gb': 1024.0 * 1024.0 * 1024.0, 'tb': 1024.0 * 1024.0 * 1024.0 * 1024.0,
                'pb': 1024.0 * 1024.0 * 1024.0 * 1024.0 * 1024.0,
                'bit': 0.125, 'kbit': 128.0, 'mbit': 131072.0,
                'gbit': 134217728.0, 'tbit': 137438953472.0
            },
            'acceleration': {
                'm/s2': 1.0, 'km/h/s': 1 / 3.6, 'ft/s2': 0.3048,
                'g': 9.80665  # standard gravity
            }
        }
        # Add aliases for square units
        self._factors['area']['sq m'] = self._factors['area']['m2']
        self._factors['area']['sq km'] = self._factors['area']['km2']
        self._factors['area']['sq cm'] = self._factors['area']['cm2']
        self._factors['area']['sq mm'] = self._factors['area']['mm2']
        self._factors['area']['sq mi'] = self._factors['area']['mi2']
        self._factors['area']['sq yd'] = self._factors['area']['yd2']
        self._factors['area']['sq ft'] = self._factors['area']['ft2']
        self._factors['area']['sq in'] = self._factors['area']['in2']
        
        # Volume aliases
        self._factors['volume']['liter'] = self._factors['volume']['l']
        self._factors['volume']['milliliter'] = self._factors['volume']['ml']
        self._factors['volume']['centiliter'] = self._factors['volume']['cl']
        self._factors['volume']['deciliter'] = self._factors['volume']['dl']
        self._factors['volume']['gallon'] = self._factors['volume']['gal']
        self._factors['volume']['quart'] = self._factors['volume']['qt']
        self._factors['volume']['pint'] = self._factors['volume']['pt']
        self._factors['volume']['cubic meter'] = self._factors['volume']['m3']
        self._factors['volume']['cubic centimeter'] = self._factors['volume']['cm3']
        self._factors['volume']['cubic millimeter'] = self._factors['volume']['mm3']

        # Data aliases
        self._factors['data']['kilobyte'] = self._factors['data']['kb']
        self._factors['data']['megabyte'] = self._factors['data']['mb']
        self._factors['data']['gigabyte'] = self._factors['data']['gb']
        self._factors['data']['terabyte'] = self._factors['data']['tb']
        self._factors['data']['petabyte'] = self._factors['data']['pb']
        self._factors['data']['kilobit'] = self._factors['data']['kbit']
        self._factors['data']['megabit'] = self._factors['data']['mbit']
        self._factors['data']['gigabit'] = self._factors['data']['gbit']
        self._factors['data']['terabit'] = self._factors['data']['tbit']
        
        # Acceleration aliases
        self._factors['acceleration']['mps2'] = self._factors['acceleration']['m/s2']
        self._factors['acceleration']['kmh/s'] = self._factors['acceleration']['km/h/s']
        self._factors['acceleration']['fps2'] = self._factors['acceleration']['ft/s2']


    def _convert(self, value, from_unit, to_unit, quantity_type):
        """Generic conversion function using factors."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if quantity_type not in self._factors:
            raise ValueError(f"Unknown quantity type: {quantity_type}")

        factors = self._factors[quantity_type]

        if from_unit not in factors or to_unit not in factors:
            valid_units = ", ".join(factors.keys())
            raise ValueError(f"Invalid unit. Valid units for {quantity_type}: {valid_units}")

        # Convert from_unit to base unit
        base_value = value * factors[from_unit]

        # Convert base unit to to_unit
        converted_value = base_value / factors[to_unit]
        return converted_value

    def convert_length(self, value, from_unit, to_unit):
        """Converts length units."""
        return self._convert(value, from_unit, to_unit, 'length')

    def convert_area(self, value, from_unit, to_unit):
        """Converts area units."""
        # Handle common alternative spellings like 'sq m'
        from_unit = from_unit.replace('sq ', '').replace('square ', '') + '2' if 'sq' in from_unit or 'square' in from_unit else from_unit
        to_unit = to_unit.replace('sq ', '').replace('square ', '') + '2' if 'sq' in to_unit or 'square' in to_unit else to_unit
        return self._convert(value, from_unit, to_unit, 'area')

    def convert_time(self, value, from_unit, to_unit):
        """Converts time units."""
        return self._convert(value, from_unit, to_unit, 'time')

    def convert_mass(self, value, from_unit, to_unit):
        """Converts mass units."""
        return self._convert(value, from_unit, to_unit, 'mass')

    def convert_velocity(self, value, from_unit, to_unit):
        """Converts velocity units."""
        return self._convert(value, from_unit, to_unit, 'velocity')
    
    def convert_volume(self, value, from_unit, to_unit):
        """Converts volume units."""
        return self._convert(value, from_unit, to_unit, 'volume')
    
    def convert_data(self, value, from_unit, to_unit):
        """Converts digital storage units."""
        return self._convert(value, from_unit, to_unit, 'data')
    
    def convert_acceleration(self, value, from_unit, to_unit):
        """Converts acceleration units."""
        return self._convert(value, from_unit, to_unit, 'acceleration')

    def convert_temperature(self, value, from_unit, to_unit):
        """Converts temperature units (Celsius, Fahrenheit, Kelvin)."""
        from_u = from_unit.lower()
        to_u = to_unit.lower()

        valid_units = ['c', 'f', 'k', 'celsius', 'fahrenheit', 'kelvin']
        if from_u not in valid_units or to_u not in valid_units:
             raise ValueError("Invalid temperature unit. Use 'C', 'F', or 'K'.")

        # Normalize units to single letters
        from_u = from_u[0]
        to_u = to_u[0]

        if from_u == to_u:
            return value

        # Convert to Celsius first (as an intermediate step)
        celsius_value = 0
        if from_u == 'c':
            celsius_value = value
        elif from_u == 'f':
            celsius_value = (value - 32) * 5 / 9
        elif from_u == 'k':
            celsius_value = value - 273.15

        # Convert from Celsius to the target unit
        if to_u == 'c':
            return celsius_value
        elif to_u == 'f':
            return (celsius_value * 9 / 5) + 32
        elif to_u == 'k':
            return celsius_value + 273.15

def get_conversion_explanation(conversion_type, from_unit, to_unit, input_value, result):
    """Generate a human-readable explanation of the conversion."""
    
    # For temperature conversions
    if conversion_type == "Temperature":
        # Use full names as received from React, map to codes if necessary for formulas
        # Or adjust formulas to use full names if backend handles them
        from_u_display = from_unit 
        to_u_display = to_unit

        # You might need to map back to 'c', 'f', 'k' if formulas rely on them
        temp_map_rev = {'celsius': 'c', 'fahrenheit': 'f', 'kelvin': 'k'}
        from_code = temp_map_rev.get(from_unit.lower(), from_unit.lower())
        to_code = temp_map_rev.get(to_unit.lower(), to_unit.lower())

        if from_code == 'c' and to_code == 'f':
            return f"Formula: °F = (°C × 9/5) + 32"
        elif from_code == 'f' and to_code == 'c':
            return f"Formula: °C = (°F - 32) × 5/9"
        elif from_code == 'c' and to_code == 'k':
            return f"Formula: K = °C + 273.15"
        elif from_code == 'k' and to_code == 'c':
            return f"Formula: °C = K - 273.15"
        elif from_code == 'f' and to_code == 'k':
            return f"Formula: K = (°F - 32) × 5/9 + 273.15"
        elif from_code == 'k' and to_code == 'f':
            return f"Formula: °F = (K - 273.15) × 9/5 + 32"
        elif from_code == to_code:
            return "Units are the same."
        else:
             return "Temperature conversion explanation unavailable." # Fallback

    # For other conversions, show the multiplication factor
    # Ensure input_value is treated as a float for division
    try:
        input_val_float = float(input_value)
        if result is not None and input_val_float != 0:
            factor = result / input_val_float
            if abs(factor - 1.0) < 1e-9: # Use tolerance for float comparison
                 return "Units are equivalent or factor is 1."
            elif factor > 1:
                # Use :.6g for general precision, avoiding excessive decimals
                return f"Conversion factor: Multiply by {factor:.6g}"
            else:
                return f"Conversion factor: Divide by {1/factor:.6g}"
        elif result is not None and input_val_float == 0:
             return "Conversion completed (input was zero)."
        else: # result might be None if conversion failed before explanation
             return "Could not determine explanation."

    except (ValueError, TypeError, ZeroDivisionError):
         # Catch potential errors during calculation
         return "Could not determine explanation due to input or calculation issue."
    
    # Default return if none of the above conditions met
    return "Conversion explanation not available."

# # --- Example Usage ---
# if __name__ == "__main__":
#     converter = UnitConverter()

#     # Length
#     feet = converter.convert_length(10, 'm', 'ft')
#     print(f"10 meters is equal to {feet:.2f} feet") # Output: 10 meters is equal to 32.81 feet

#     # Area
#     acres = converter.convert_area(1, 'km2', 'ac')
#     print(f"1 square kilometer is equal to {acres:.2f} acres") # Output: 1 square kilometer is equal to 247.11 acres
#     sq_ft = converter.convert_area(5, 'sq m', 'sq ft')
#     print(f"5 square meters is equal to {sq_ft:.2f} sq ft") # Output: 5 square meters is equal to 53.82 sq ft

#     # Time
#     minutes = converter.convert_time(2, 'hr', 'min')
#     print(f"2 hours is equal to {minutes:.0f} minutes") # Output: 2 hours is equal to 120 minutes

#     # Mass
#     pounds = converter.convert_mass(5, 'kg', 'lb')
#     print(f"5 kilograms is equal to {pounds:.2f} pounds") # Output: 5 kilograms is equal to 11.02 pounds

#     # Velocity
#     mph = converter.convert_velocity(60, 'km/h', 'mph')
#     print(f"60 km/h is equal to {mph:.2f} mph") # Output: 60 km/h is equal to 37.28 mph

#     # Temperature
#     fahrenheit = converter.convert_temperature(25, 'C', 'F')
#     print(f"25 Celsius is equal to {fahrenheit:.1f} Fahrenheit") # Output: 25 Celsius is equal to 77.0 Fahrenheit

#     celsius = converter.convert_temperature(50, 'F', 'C')
#     print(f"50 Fahrenheit is equal to {celsius:.1f} Celsius") # Output: 50 Fahrenheit is equal to 10.0 Celsius

#     kelvin = converter.convert_temperature(100, 'C', 'K')
#     print(f"100 Celsius is equal to {kelvin:.2f} Kelvin") # Output: 100 Celsius is equal to 373.15 Kelvin

#     # Volume
#     gallons = converter.convert_volume(10, 'l', 'gal')
#     print(f"10 liters is equal to {gallons:.2f} gallons") # Output: 10 liters is equal to 2.64 gallons

#     cups = converter.convert_volume(500, 'ml', 'cup')
#     print(f"500 milliliters is equal to {cups:.2f} cups") # Output: 500 milliliters is equal to 2.08 cups

#     # Data
#     megabytes = converter.convert_data(1024, 'kb', 'mb')
#     print(f"1024 kilobytes is equal to {megabytes:.2f} megabytes") # Output: 1024 kilobytes is equal to 1.00 megabytes

#     gigabits = converter.convert_data(8, 'gb', 'gbit')
#     print(f"8 gigabytes is equal to {gigabits:.2f} gigabits") # Output: 8 gigabytes is equal to 64.00 gigabits

#     # Acceleration
#     g_force = converter.convert_acceleration(9.81, 'm/s2', 'g')
#     print(f"9.81 m/s² is equal to {g_force:.2f} g") # Output: 9.81 m/s² is equal to 1.00 g

#     fps2 = converter.convert_acceleration(2, 'g', 'ft/s2')
#     print(f"2 g is equal to {fps2:.2f} ft/s²") # Output: 2 g is equal to 64.34 ft/s²

#     # Example of invalid unit
#     try:
#         converter.convert_length(10, 'm', 'lightyear')
#     except ValueError as e:
#         print(f"Error: {e}") # Output: Error: Invalid unit. Valid units for length: m, km, cm, mm, mi, yd, ft, in, nmi 