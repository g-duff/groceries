from typing import List
from pathlib import Path
from databaseLayer import databaseService
import groceries

def load(fpath):
    with open(fpath, 'r') as open_meal:
        ingredient_list = [groceries.Ingredient(*line.split(',')) for line in open_meal]
    return ingredient_list


def mealList(recipePath = "databaseLayer/recipes"):
    return [f for f in Path(recipePath).glob("*") if f.is_file()]

if __name__ == '__main__':
    DatabaseService = databaseService.DatabaseService()

    mealPaths: List[Path] = mealList()

    for mealPath in mealPaths:
        ingredientsList:List = load(mealPath)
        mealName:str = mealPath.stem
        DatabaseService.insertRecipeToDatabase(mealName, ingredientsList)

    DatabaseService.commitAndClose()