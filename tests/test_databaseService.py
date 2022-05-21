import unittest
from database import databaseService

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

        questionList = databaseService.load("databaseLayer/recipes/chilli.csv")
        questionStr = [str(i) for i in questionList]

        self.assertEqual(questionStr, inString)