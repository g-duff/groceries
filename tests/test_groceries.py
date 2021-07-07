import groceries as gc  # The code to test
import unittest         # The test framework


class TestIngredients(unittest.TestCase):

    def test_toString(self):
        '''Ingredients class returns proper string'''
        ingredient = gc.Ingredient("Potato", 2, "#", "veg")

        self.assertEqual("2.0 # of potato", str(ingredient))


class TestGroceries(unittest.TestCase):

    def test_load(self):
        ''' Load a recipe from a filepath'''

        inString = [
            "1.0 tin of tinned tomatoes",
            "1.0 tin of kidney beans",
            "1.0 tin of black beans",
            "1.0 # of onion",
            "1.0 cloves of garlic"
        ]

        questionList = gc.load("recipes/chilli.csv")
        questionStr = [str(i) for i in questionList]

        self.assertEqual(questionStr, inString)
 

    def test_getCategories(self):
        '''Get items in a given category'''

        names = ("potato", "tomato", "eggs", "milk")
        quantities = (2, 4, 6, 1)
        units = ("#", "#", "#", "l")
        categogires = ("veg", "veg", "dairy", "dairy")
        inputArgs = zip(names, quantities, units, categogires)

        inputList = [gc.Ingredient(*a) for a in inputArgs]
        shoppingList = gc.ShoppingList(inputList)


        vegList = shoppingList.getCategory("veg")
        boolList = [(v.category == "veg") for v in vegList]
        
        self.assertTrue(all(boolList))


    def test_sumDuplicates(self):
        '''Sum duplicate ingredients'''
        names = ("potato", "tomato", "cabbage", "potato", "cabbage")
        quantities = range(1, 6)
        units = ("#" for i in range(1, 6))
        categories = ("veg" for i in range(1, 6))

        inputArgs = zip(names, quantities, units, categories)

        questionList = gc.ShoppingList([gc.Ingredient(*a) for a in inputArgs])
        questionList.sumDuplicates()

        answerString = "8.0 # of cabbage\n5.0 # of potato\n2.0 # of tomato"

        self.assertEqual(str(questionList), answerString)


if __name__ == '__main__':
    unittest.main()