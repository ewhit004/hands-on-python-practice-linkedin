#"flask" is a package that allows you to easily get things from the web
from flask import Flask

#instantiate a flask object with dunderscore
app = Flask(__name__)

#define routes w/ decorators
@app.route("/") #decorator
def hello():
  return "Hello, World!"

#This will display a mock website page with the words "Hello, World!" on it

app.run(debug=True)