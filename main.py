from flask import Flask, render_template, request
from utils.processor import BuildCV

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_dat = request.form.to_dict()
        cv = BuildCV("utils/build.html")
        cv.populate(form_dat)
    return render_template("website/index.html")


@app.route("/build", methods=["GET"])
def build():
    return render_template("website/build.html")


app.run(debug=True)
