# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
# Assuming unit_converter.py contains the UnitConverter class and get_conversion_explanation
from unit_converter import UnitConverter, get_conversion_explanation

app = Flask(__name__)
CORS(app) # Allow requests from your React app's origin (e.g., localhost:3000)

converter = UnitConverter()

# --- Add get_conversion_explanation function here if not in unit_converter.py ---
# Make sure this function is available
# def get_conversion_explanation(conversion_type, from_unit, to_unit, input_value, result):
#     # ... (copy the function implementation from unit_converter_app.py) ...
#     # Ensure it uses the correct logic based on the backend's UnitConverter class
#     if conversion_type == "Temperature":
#         from_u = from_unit.lower()
#         to_u = to_unit.lower()
        
#         # Use the single letter codes expected by convert_temperature
#         from_code = from_u[0] if from_u in ['celsius', 'fahrenheit', 'kelvin'] else from_u
#         to_code = to_u[0] if to_u in ['celsius', 'fahrenheit', 'kelvin'] else to_u

#         if from_code == 'c' and to_code == 'f':
#             return f"Formula: °F = (°C × 9/5) + 32"
#         elif from_code == 'f' and to_code == 'c':
#             return f"Formula: °C = (°F - 32) × 5/9"
#         elif from_code == 'c' and to_code == 'k':
#             return f"Formula: K = °C + 273.15"
#         elif from_code == 'k' and to_code == 'c':
#             return f"Formula: °C = K - 273.15"
#         elif from_code == 'f' and to_code == 'k':
#             return f"Formula: K = (°F - 32) × 5/9 + 273.15"
#         elif from_code == 'k' and to_code == 'f':
#             return f"Formula: °F = (K - 273.15) × 9/5 + 32"
#         elif from_code == to_code:
#              return "Units are the same."

#     # For other conversions, show the multiplication factor
#     if input_value != 0 and result is not None: # Check result is not None
#         try:
#             factor = result / float(input_value)
#             if factor == 1.0:
#                  return "Units are equivalent or factor is 1."
#             elif factor > 1:
#                 return f"Conversion factor: Multiply by {factor:.6g}"
#             else:
#                 return f"Conversion factor: Divide by {1/factor:.6g}"
#         except ZeroDivisionError:
#              return "Input value is zero."
#     elif result is not None:
#          return "Conversion completed (input was zero)."
#     return "Could not determine explanation." # Default case
# ---------------------------------------------------------------------------


# api.py - inside get_units() function
@app.route('/units', methods=['GET'])
def get_units():
    """Returns the available units for each conversion type."""
    units_data = {}
    for type_name, factors in converter._factors.items():
        # --- START MODIFICATION ---
        if type_name == 'data':
            # For 'data', sort keys based on their corresponding factor value (size)
            # This sorts based on the numerical value associated with the unit key
            sorted_keys = sorted(factors.keys(), key=lambda k: factors[k])
        else:
            # For all other types, sort alphabetically (default)
            sorted_keys = sorted(list(factors.keys()))
        units_data[type_name.capitalize()] = sorted_keys
        # --- END MODIFICATION ---

    # Add Temperature separately with full names (already logically ordered)
    units_data['Temperature'] = ['Celsius', 'Fahrenheit', 'Kelvin']

    return jsonify(units_data)


@app.route('/convert', methods=['POST'])
def convert():
    """Performs a unit conversion."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    conv_type = data.get('type')
    value_str = data.get('value')
    from_unit = data.get('fromUnit')
    to_unit = data.get('toUnit')

    if not all([conv_type, value_str is not None, from_unit, to_unit]):
        return jsonify({"error": "Missing required fields (type, value, fromUnit, toUnit)"}), 400

    try:
        value = float(value_str)
    except ValueError:
        return jsonify({"error": "Invalid input value, must be a number"}), 400

    # Map frontend type name (e.g., "Length") to backend key (e.g., "length")
    type_key = conv_type.lower()

    result = None
    explanation = "Error during conversion."

    try:
        if type_key == 'temperature':
            # Map full names back to codes if needed by the backend function
            from_unit_code = from_unit # Assume backend handles 'Celsius', etc. or map here
            to_unit_code = to_unit
            # If backend expects 'c', 'f', 'k':
            # temp_map_reverse = {'celsius': 'c', 'fahrenheit': 'f', 'kelvin': 'k'}
            # from_unit_code = temp_map_reverse.get(from_unit.lower(), from_unit)
            # to_unit_code = temp_map_reverse.get(to_unit.lower(), to_unit)
            result = converter.convert_temperature(value, from_unit_code, to_unit_code)
        elif type_key in converter._factors:
            # Dynamically find the correct conversion method if needed
            # Or use the generic _convert (simpler if backend class structure allows)
            method_name = f"convert_{type_key}"
            if hasattr(converter, method_name):
                 convert_func = getattr(converter, method_name)
                 result = convert_func(value, from_unit, to_unit)
            else:
                 # Fallback or raise error if specific method needed but not found
                 # Assuming _convert can handle it based on type_key
                 result = converter._convert(value, from_unit, to_unit, type_key)
        else:
            return jsonify({"error": f"Unknown conversion type: {conv_type}"}), 400

        # Get explanation using the function (ensure it's accessible)
        explanation = get_conversion_explanation(conv_type, from_unit, to_unit, value, result)

        return jsonify({
            "result": result,
            "explanation": explanation
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Catch broader exceptions for unexpected errors
        app.logger.error(f"Conversion error: {e}", exc_info=True) # Log the full error
        return jsonify({"error": "An internal server error occurred."}), 500


if __name__ == '__main__':
    # Make sure to use a different port than the React dev server (default 3000)
    app.run(debug=True, port=5001)