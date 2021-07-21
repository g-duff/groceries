import groceries as gc  # The code to test
import unittest         # The test framework

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

inputDiv   = "body > div > div:nth-child(2)"
inputItem  = "body > div > div:nth-child(2) > form > p:nth-child(1)"
inputItems = "body > div > div:nth-child(2) > form > p"

class TestUI(unittest.TestCase):


    def setUp(self) -> None:
        ''' Creates a common webdriver, visits the page in browser'''
        try:
            driver = webdriver.Chrome(executable_path='./chromedriver')
        except:
            driver = webdriver.Safari()
            
        self.driver = driver
        self.driver.get("http://127.0.0.1:5000")

        return super().setUp()


    def tearDown(self) -> None:
        ''' Close the selenium webdriver'''
        self.driver.close()
        return super().tearDown()


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

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, inputItems))
        )
        
        inputBoxes = self.driver.find_elements_by_css_selector(inputItems)

        pageInputFields = [ib.text for ib in inputBoxes]
        pageInputFields.sort()

        designedInputFields = gc.mealList()
        designedInputFields = sorted(f.stem.replace("_", " ") for f in designedInputFields)

        self.assertEqual(pageInputFields, designedInputFields)

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


    def test_emptyList(self):
        ''' generate a list of ingredients without any recipes selected '''
        # Subut form

        # Compare with selected output
        pass