import csv
#allows you to render certain file type (HTML file in this case)
from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    #"jsonify()" turns all laureate dictionaries into json types
    return jsonify(laureates)

#creates a web application that displays all laureates and information
#about them, but it lacks functionality back buttons and search buttons

app.run(debug=True)
