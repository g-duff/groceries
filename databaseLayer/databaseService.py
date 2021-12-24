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

    def __init__(self, databasePath: Path):
        self.databasePath: Path = databasePath
        self.connection: sqlite3.Connection = sqlite3.connect(databasePath)
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        pass
