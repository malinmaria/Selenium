import unittest
from selenium import webdriver


class TestHomePage(unittest.TestCase):
    def test_openHP(self):
        driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")
        driver.get("https://www.pennmedicine.org/cosmetic-services")
        print("Title is : " + driver.title)


if __name__ == '__main__':
    unittest.main()




