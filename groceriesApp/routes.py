from flask.templating import render_template
from flask import request
from groceriesApp import app
import groceries as gc
from databaseLayer import databaseService

@app.route("/", methods=["GET", "POST"])
@app.route("/combine-recipes", methods=["GET", "POST"])
def home():
    mealList = databaseService.mealList()
    
    if request.method == "POST":

        # Load user-specified ingredients
        inList = []
        for recipePath in request.form:
            inList += databaseService.load(recipePath)

        # Process the ingredients 
        shoppingList = gc.ShoppingList(inList)
        shoppingList.sumDuplicates()

        # Split into categories
        shoppingDict = shoppingList.getCategories()
        
        return render_template("./combine-recipes.html", mealList=mealList, shoppingDict=shoppingDict)
    
    elif request.method == "GET":
        return render_template("./combine-recipes.html", mealList=mealList, shoppingDict={})


@app.route("/enter_recipe")
def enter_recipe():
    return render_template("./enter-recipe.html")