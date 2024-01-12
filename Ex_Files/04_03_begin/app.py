import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    
    #empty list of laureates
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    #if a surname param is available, then use the search_string variable
    #lower() ensures a looser match and strip() cleans up the search
    search_string = request.args.get("surname").lower().strip()

    #run through each laureate
    for laureate in laureates:
        #checking if search_string is inside of laureates lowercase surname
        if search_string in laureate["surname"].lower():
            results.append(laureate)
    return jsonify(results)


app.run(debug=True)
