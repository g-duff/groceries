import groceries as gc  # The code to test
import unittest         # The test framework

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

inputDiv   = "body > div > div:nth-child(2)"
inputItems = "body > div > div:nth-child(2) > form > p > label"
submItems  = "body > div > div:nth-child(2) > form > button"

outputDiv  = "body > div > div:nth-child(3)"
outputItem = "body > div > div:nth-child(3) > ul > li"

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

        testRecipe = "chilli"

        sl = gc.ShoppingList(gc.load(f"./recipes/{testRecipe}.csv"))
        sl.sumDuplicates()
        expectedOutput = sl.getCategories()

        outString = []
        for category, items in expectedOutput.items():
            outString.append(category)
            for i in items:
                outString.append(str(i))

        # Tick a single box
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, inputItems))
        )
        inputBoxes = self.driver.find_elements_by_css_selector(inputItems)
        for ib in inputBoxes:
            if ib.text == testRecipe:
                ib.click()

        # Submit form
        submitButton = self.driver.find_element_by_css_selector(submItems)
        submitButton.location_once_scrolled_into_view
        submitButton.click()

        # Compare text output with expected output
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, outputItem))
        )
        outputSList = self.driver.find_elements_by_css_selector(outputItem)
        actualOutput = [ao.text for ao in outputSList]

        self.assertEqual(outString, actualOutput)


    def test_combineRecipes(self):
        ''' Compares combined ingredients from multiple recipes on page 
        with expected output text'''
        # Tick boxes

        # Submit form

        # Compare text output with expected output
        pass


    def test_emptyList(self):
        ''' generate a list of ingredients without any recipes selected '''
        # Submit form
        submitButton = self.driver.find_element_by_css_selector(submItems)
        submitButton.location_once_scrolled_into_view
        submitButton.click()

        # Compare with selected output
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, outputItem))
        )
        outputSList = self.driver.find_elements_by_css_selector(outputItem)
        actualOutput = [ao.text for ao in outputSList]

        self.assertEqual(["Empty list"], actualOutput)