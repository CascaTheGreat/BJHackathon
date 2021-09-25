from flask import Flask
from flask import render_template
from flask import request
import model

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
@app.route("/map")
def map():
  return render_template("map.html")
@app.route("/result", methods=["GET", "POST"])
def result():
  if request.method == "POST":
    diagList = model.output(request.form)
    return(render_template("result.html", diagnosis1 = diagList[0], diagnosis2 = diagList[2], diagnosis1link=diagList[1], diagnosis2link=diagList[3])) 
  else:
    return "Sorry, there was an error."
if __name__ == "__main__":
  app.run()
