import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.pennmedicine.org/cosmetic-services/request-cosmetic-services-consult')

    def test_populateForm(self):
        time.sleep(3)
        iframe = self.driver.find_element_by_id("pcmaincontent_0_ctl02_divFormContainer").find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "tfa_52").send_keys("Test First Name")
        self.driver.find_element(By.ID, "tfa_53").send_keys("Test Last Name")
        dob = self.driver.find_element(By.ID, "tfa_54")
        dob.click()
        dob.send_keys("01011999")
        phone = self.driver.find_element(By.ID, "tfa_55")
        phone.click()
        phone.send_keys("1231231234")
        self.driver.find_element(By.ID, "tfa_56").send_keys("21211")
        self.driver.find_element(By.ID, "tfa_57").send_keys("test@mail.com")
        self.driver.find_element(By.ID, "tfa_72").send_keys("Typing in a test reason")
        #self.driver.find_element_by_class_name("input-checkbox-faux").click()
        self.driver.find_element_by_id("submit_button").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "b").text == "Thank you for your request"


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
