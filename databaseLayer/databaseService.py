from typing import List
from pathlib import Path
import sqlite3
import groceries 

def load(fpath):
    with open(fpath, 'r') as open_meal:
        ingredient_list = [groceries.Ingredient(*line.split(',')) for line in open_meal]
    return ingredient_list


def mealList(recipePath = "databaseLayer/recipes"):
    return [f for f in Path(recipePath).glob("*") if f.is_file()]


class DatabaseService():

    def __init__(self, databasePath: Path = Path("./recipes.db")):
        self.databasePath: Path = databasePath
        self.connection: sqlite3.Connection = sqlite3.connect(databasePath)
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def getMealList(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        formattedNames = [rawName[0] for rawName in self.cursor.fetchall()]
        return formattedNames

    def insertRecipeToDatabase(self, mealName: str, ingredients: List):
        mealIsNew: bool = True
        try:
            self.createRecipe(mealName)
        except (sqlite3.OperationalError) as thrownException:
            mealIsNew = False

        if mealIsNew:
            self._insertRecipeIntoDatabase(mealName, ingredients)

    def createRecipe(self, mealName:str):
        self.cursor.execute(f'CREATE TABLE {mealName} (ingredient text, amount real, quantity text, category text)')
           
    def _insertRecipeIntoDatabase(self, mealName: str, ingredients: List):
        for ingredient in ingredients:
            self.cursor.execute(f"INSERT INTO {mealName} VALUES ('{ingredient.name}',{ingredient.quantity},'{ingredient.unit}','{ingredient.category}')")

    def commitAndClose(self):
        self.commitChanges()
        self.closeConnection()

    def commitChanges(self):
        self.connection.commit()
    
    def closeConnection(self):
        self.connection.close()
