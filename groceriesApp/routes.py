from flask.templating import render_template
from flask import request
from groceriesApp import app
import groceries as gc
from database import databaseService

@app.route("/", methods=["GET", "POST"])
@app.route("/combine-recipes", methods=["GET", "POST"])
def home():
    DatabaseService = databaseService.DatabaseService()
    shoppingDict = {}
    
    if request.method == "POST":

        # Load user-specified ingredients
        inList = []
        for mealName in request.form:
            inList += DatabaseService.getMealIngredients(mealName)

        # Process the ingredients 
        shoppingList = gc.ShoppingList(inList)
        shoppingList.sumDuplicates()

        # Split into categories
        shoppingDict = shoppingList.getCategories()

    mealList = DatabaseService.getMealList()
    DatabaseService.closeConnection()
    return render_template("./combine-recipes.html", mealList=mealList, shoppingDict=shoppingDict)


@app.route("/enter_recipe")
def enter_recipe():
    return render_template("./enter-recipe.html")