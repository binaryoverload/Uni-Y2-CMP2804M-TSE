import flask
import json

app = flask.Flask(__name__)

#all covid data
@app.route('/covid/<date>')
def covid(date):
    with open('./covid-data-jan-dec.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[date])

#all flight data
@app.route('/flight/<icao24>')
def flight(icao24):
    with open('./flight-data-jan-dec.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[icao24])

#flight data for airports
@app.route('/flight/airport/<icao24>')
def flight_airports(icao24):
    with open('./flight-data-airports.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[icao24])

#county data for covid cases
@app.route('/covid/counties/<areaCode>')
def counties(areaCode):
    with open('./flight-data-airports.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[areaCode])

#flight data for international
@app.route('/flight/international/<icao24>')
def flight_international(icao24):
    with open('./flight-data-international.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[icao24])

if __name__ == "__main__":
    app.run(debug=True)