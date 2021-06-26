from re import template
from flask.templating import render_template
from groceriesApp import app

@app.route("/")
@app.route("/combine-recipes")
def combine_recipe():
    return render_template("./combine-recipes.html")


@app.route("/enter_recipe")
def enter_recipe():
    return render_template("./enter-recipe.html")