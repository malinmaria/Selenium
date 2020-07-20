import unittest
from selenium import webdriver


class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.pennmedicine.org/cosmetic-services")

    def test_openHP(self):
        print("Title is " + self.driver.title)
        assert self.driver.title == "Penn Medicine Cosmetic Services – Penn Cosmetics"

    def test_navLinks(self):
        # Procedures > Skin
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_0").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_0").click()
        assert self.driver.title == "Cosmetic Procedures – Penn Cosmetics"
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_0").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_rptSecondaryNav_0_lnkSecondaryNavItem_3").click()
        assert self.driver.title == "Skin Care Treatments – Penn Cosmetics"
        # Why Penn > Client Testimonials
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_1").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_1").click()
        assert self.driver.title == "The Penn Cosmetic Surgery Difference – Penn Cosmetics"
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_1").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_rptSecondaryNav_1_lnkSecondaryNavItem_1").click()
        assert self.driver.title == "Client Testimonials – Penn Cosmetics"
        # Meet the Team
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_2").click()
        assert self.driver.title == "Meet the Penn Cosmetic Surgery Team – Penn Cosmetics"
        # Before & After
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_3").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_3").click()
        assert self.driver.title == "Photos of Before and After Cosmetic Procedures – Penn Cosmetics"
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_spNavItemTitle_3").click()
        self.driver.find_element_by_id("ctl05_rptPrimaryNav_rptSecondaryNav_3_lnkSecondaryNavItem_1").click()
        assert self.driver.title == "Before & After: Face Procedures – Penn Cosmetics"
        # Cosmetic Home
        self.driver.find_element_by_class_name("nav__level1-toggle-text").click()
        assert self.driver.title == "Penn Medicine Cosmetic Services – Penn Cosmetics"


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




