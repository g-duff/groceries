from pathlib import Path
import groceries 

def load(fpath):
    with open(fpath, 'r') as open_meal:
        ingredient_list = [groceries.Ingredient(*line.split(',')) for line in open_meal]
    return ingredient_list


def mealList(recipePath = "recipes"):
    P = Path(recipePath)
    return [f for f in P.glob("*") if f.is_file()]
