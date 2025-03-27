# Universal Unit Converter

A comprehensive unit conversion application with a Python backend and React frontend. This project allows for conversions between different units of length, area, volume, mass, time, velocity, acceleration, temperature, and data.

## Features

- **Comprehensive Unit Support**: Convert between various units across multiple categories:
  - Length (meters, feet, inches, etc.)
  - Area (square meters, acres, etc.)
  - Volume (liters, gallons, etc.)
  - Mass (kilograms, pounds, etc.)
  - Time (seconds, minutes, hours, etc.)
  - Velocity (m/s, km/h, mph, etc.)
  - Acceleration (m/s², g-force, etc.)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Data Storage (bytes, kilobytes, megabytes, etc.)

- **Dual Implementation**:
  - Standalone Python class for direct use in Python code
  - Flask API backend with React frontend for web use

- **User-Friendly Interfaces**:
  - Clean, responsive React UI with Tailwind CSS and DaisyUI
  - Interactive Streamlit interface as an alternative

## Project Structure

```
.
├── unit_converter.py          # Core Python conversion library
├── unit_converter_app.py      # Streamlit application
├── api.py                     # Flask API server
└── unit-converter-frontend/   # React frontend
    ├── public/
    ├── src/
    ├── package.json
    ├── tailwind.config.js
    └── postcss.config.js
```

## Backend (Python)

### Core Conversion Library

The `UnitConverter` class in `unit_converter.py` provides the core functionality for all unit conversions:

```python
# Example usage
from unit_converter import UnitConverter

converter = UnitConverter()
# Convert 5 kilometers to miles
miles = converter.convert_length(5, 'km', 'mi')
print(f"5 kilometers is {miles:.2f} miles")

# Convert 20 Celsius to Fahrenheit
fahrenheit = converter.convert_temperature(20, 'C', 'F')
print(f"20°C is {fahrenheit:.1f}°F")
```

### Flask API

The Flask API (`api.py`) exposes the unit converter functionality as a RESTful web service:

- `GET /units` - Returns all available units by category
- `POST /convert` - Performs a conversion based on posted data

To run the API server:

```bash
pip install flask flask-cors
python api.py
```

The server runs on `http://localhost:5001` by default.

## Frontend (React)

The React frontend provides a responsive, modern web interface.

### Setup and Installation

```bash
cd unit-converter-frontend
npm install
npm start
```

The development server runs on `http://localhost:3000`.

### Features

- Responsive design using Tailwind CSS and DaisyUI
- Real-time conversion as inputs change
- Formula explanations for each conversion
- Unit selection from categorized dropdowns
- Mobile-friendly UI

### Building for Production

```bash
cd unit-converter-frontend
npm run build
```

## Running the Complete Application

1. Start the Python API server:
   ```bash
   python api.py
   ```

2. In a separate terminal, start the React frontend:
   ```bash
   cd unit-converter-frontend
   npm start
   ```

3. Open your browser to `http://localhost:3000`

## Dependencies

### Python
- Flask (for API)
- flask-cors (for CORS support)

### Frontend
- React 
- Tailwind CSS
- DaisyUI
- PostCSS

## License

MIT

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## Acknowledgements

This project was inspired by the need for a comprehensive unit conversion tool that handles various units across different domains. 
