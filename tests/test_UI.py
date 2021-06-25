import groceries as gc  # The code to test
import unittest         # The test framework


class TestUI(unittest.TestCase):

    def setUp(self) -> None:
        '''Runs the flask application, visits the page in chrome'''
        return super().setUp()


    def test_saveRecipe(self):
        '''Compares text input to recipe with saved file in backend'''

        # Enter recipe onto webpage

        # Execute the save function

        # Check if the recipe has been saved in that location,
        # that the contents of the saved file is correct

        pass

    
    def test_generateSelectPage(self):
        '''Generates and presents correct input checkboxes in html.
        Compares with available recipes in database'''
        pass

    def test_loadRecipe(self):
        ''' Compares presented ingredients from a single recipe on page 
        with expected output text'''
        # Tick a single box

        # Submit form

        # Compare text output with expected output
        pass


    def test_combineRecipes(self):
        ''' Compares combined ingredients from multiple recipes on page 
        with expected output text'''
        # Tick boxes

        # Submit form

        # Compare text output with expected output
        pass