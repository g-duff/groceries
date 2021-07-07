from pathlib import Path

def load(fpath):
    with open(fpath, 'r') as open_meal:
        ingredient_list = [Ingredient(*line.split(',')) for line in open_meal]
    return ingredient_list


def mealList(recipePath = "recipes"):
    P = Path(recipePath)
    return [f for f in P.glob("*") if f.is_file()]


class Ingredient:

    def __init__(self, name, quantity, unit, category, meal=None):
        self.name = name.strip().lower()
        self.quantity = float(quantity)
        self.unit = unit.strip()
        self.category = category.strip().lower()
        try:
            self.meal = meal.strip().lower()
        except AttributeError:
            self.meal = None


    def __str__(self) -> str:
        return f"{self.quantity} {self.unit} of {self.name}"


    def __repr__(self) -> str:
        return f"Ingredient({self.name}, {self.quantity}, {self.unit}, \
            {self.category}, {self.meal}"
        pass
    

class ShoppingList:

    def __init__(self, items):
        self.items = items


    def getCategory(self, catgory):
        categorizedItems = [i for i in self.items if i.category==catgory]
        return categorizedItems


    def getCategories(self, templateDict={"veg": [], "dairy": []}):
        
        for i in self.items:
            if i.category in templateDict:
                templateDict[i.category].append(i)
            else:
                templateDict[i.category] = [i]

        return templateDict


    def sumDuplicates(self) -> None:

        self.items.sort(key= lambda i: i.name)

        for i in range(len(self.items)-1, 0, -1):
            if self.items[i-1].name == self.items[i].name:
                self.items[i-1].quantity += self.items[i].quantity
                del self.items[i]


    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.items)


    def append(self, appendList) -> None : 
        self.items.append(appendList.items)