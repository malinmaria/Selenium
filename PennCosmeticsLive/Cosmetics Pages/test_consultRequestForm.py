import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.pennmedicine.org/cosmetic-services/request-cosmetic-services-consult')

    def test_populateForm(self):
        self.driver.find_element_by_id('tfa_52-L').send_keys("Test First Name")
        

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
