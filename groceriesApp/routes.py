from flask.templating import render_template
from flask import request
from groceriesApp import app
import groceries as gc

@app.route("/", methods=["GET", "POST"])
@app.route("/combine-recipes", methods=["GET", "POST"])
def home():
    mealList = gc.mealList()
    
    if request.method == "POST":

        # Load user-specified ingredients
        inList = []
        for recipePath in request.form:
            inList += gc.load(recipePath)

        # Process the ingredients
        shoppingList = gc.ShoppingList(inList)
        shoppingList.sumDuplicates()

        # Split into categories
        
        return render_template("./combine-recipes.html", mealList=mealList, ingredients=shoppingList.items)
    
    elif request.method == "GET":
        return render_template("./combine-recipes.html", mealList=mealList)


@app.route("/enter_recipe")
def enter_recipe():
    return render_template("./enter-recipe.html")