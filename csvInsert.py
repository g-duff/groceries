from typing import List
from pathlib import Path
from databaseLayer import databaseService

if __name__ == '__main__':
    DatabaseService = databaseService.DatabaseService()

    mealPaths: List[Path] = databaseService.mealList()

    for mealPath in mealPaths:
        ingredientsList:List = databaseService.load(mealPath)
        mealName:str = mealPath.stem
        DatabaseService.insertRecipeToDatabase(mealName, ingredientsList)

    DatabaseService.commitAndClose()