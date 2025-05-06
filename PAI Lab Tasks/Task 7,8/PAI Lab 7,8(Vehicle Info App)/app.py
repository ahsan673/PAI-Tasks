from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    vehicle_data = None
    error = None
    if request.method == 'POST':
        vin = request.form['vin'].strip()
        if len(vin) != 17:
            error = "VIN must be exactly 17 characters long."
        else:
            url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesExtended/{vin}?format=json"
            try:
                response = requests.get(url)
                results = response.json()['Results'][0]
                vehicle_data = {
                    'Make': results.get('Make', 'N/A'),
                    'Model': results.get('Model', 'N/A'),
                    'Year': results.get('ModelYear', 'N/A'),
                    'Fuel Type': results.get('FuelTypePrimary', 'N/A'),
                    'Engine': results.get('EngineModel', 'N/A'),
                    'Class': results.get('VehicleType', 'N/A')
                }
            except Exception as e:
                error = "Failed to fetch vehicle data."
    return render_template('index.html', vehicle=vehicle_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
