from typing import List
from pathlib import Path
import sqlite3
import groceries 

class DatabaseService():

    def __init__(self, databasePath: Path = Path("./databaseLayer/recipes.db")):
        self.databasePath: Path = databasePath
        self.connection: sqlite3.Connection = sqlite3.connect(databasePath)
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def getMealList(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        formattedNames = [rawName[0] for rawName in self.cursor.fetchall()]
        return formattedNames

    def getMealIngredients(self, mealName:str):
        self.cursor.execute(f"SELECT ingredient, amount, quantity, category FROM {mealName}")
        return [groceries.Ingredient(*line) for line in self.cursor]

    def insertRecipeToDatabase(self, mealName: str, ingredients: List):
        if not self.checkMealExists():
            self._insertRecipeIntoDatabase(mealName, ingredients)

    def checkMealExists(self, mealName: str):
        return mealName in set(self.getMealList())

    def _insertRecipeIntoDatabase(self, mealName: str, ingredients: List):
        self.createRecipe(mealName)
        for ingredient in ingredients:
            self.cursor.execute(f"INSERT INTO {mealName} VALUES ('{ingredient.name}',{ingredient.quantity},'{ingredient.unit}','{ingredient.category}')")

    def createRecipe(self, mealName:str):
        self.cursor.execute(f'CREATE TABLE {mealName} (ingredient text, amount real, quantity text, category text)')

    def commitAndClose(self):
        self.commitChanges()
        self.closeConnection()

    def commitChanges(self):
        self.connection.commit()
    
    def closeConnection(self):
        self.connection.close()
