from flask import Flask, render_template
app = Flask(__name__)

# HOME
@app.route('/')
def index():
    
    return render_template("index.html")

# SEARCH
@app.route('/search')
def search_ingredient():
    
    return render_template("search_t.html")

# SETTINGS
@app.route('/settings')
def settings():
    
    return render_template("settings_t.html")

# RECIPE / ROULETTE
@app.route('/recipe')
def db_recipe_page():
    
    return render_template("recipe_t.html")
