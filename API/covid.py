import flask
import json

app = flask.Flask(__name__)

@app.route('/covid/<date>')
def covid(date):
    with open('./covid-data-jan-dec.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[date])

if __name__ == "__main__":
    app.run(debug=True)