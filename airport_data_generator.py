# airport_data_generator.py
import csv

# Open the CSV file
with open('airport-codes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Initialize the airport data dictionary
    airport_data = {}
    
    # Skip the header row if present
    next(reader, None)
    
    # Iterate over each row in the CSV
    for row in reader:
        code, name, country_code = row
        
        # Add the airport code, name, and country code to the dictionary
        airport_data[code] = {
            "name": name,
            "countryCode": country_code
        }
    
    # Generate the JavaScript object string
    js_object = 'const airportData = {\n'
    for code, airport_info in airport_data.items():
        name = airport_info['name']
        country_code = airport_info['countryCode']
        js_object += f'  "{code}": {{\n    "name": "{name}",\n    "countryCode": "{country_code}"\n  }},\n'
    js_object += '};'
    
    # Write the JavaScript object to a file
    with open('airportData.js', 'w') as jsfile:
        jsfile.write(js_object)