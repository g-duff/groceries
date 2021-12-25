from typing import List
from pathlib import Path
from databaseLayer import databaseService

if __name__ == '__main__':
    DatabaseService = databaseService.DatabaseService(Path('databaseLayer/recipes.db'))

    mealPaths: List[Path] = databaseService.mealList()

    for mealPath in mealPaths:
        ingredientsList = databaseService.load(mealPath)
        mealName = mealPath.stem
        DatabaseService.insertRecipeToDatabase(mealName, ingredientsList)

    DatabaseService.commitAndClose()