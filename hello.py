from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    headline_py = "FAT Turkey"
    return render_template("index.html", headline=headline_py)

