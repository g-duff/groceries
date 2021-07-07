from flask.templating import render_template
from flask import request
from groceriesApp import app
import groceries as gc

@app.route("/", methods=["GET", "POST"])
@app.route("/combine-recipes", methods=["GET", "POST"])
def home():
    mealList = gc.ShoppingList.mealList()
    
    if request.method == "POST":
        f = request.form
        shoppingList = gc.ShoppingList([]) # Placeholder
        return render_template("./combine-recipes.html", mealList=mealList, ingredients=shoppingList.items)
    
    elif request.method == "GET":
        return render_template("./combine-recipes.html", mealList=mealList)


@app.route("/enter_recipe")
def enter_recipe():
    return render_template("./enter-recipe.html")