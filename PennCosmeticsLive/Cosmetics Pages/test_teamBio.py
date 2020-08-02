import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TeamBioPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.pennmedicine.org/cosmetic-services/meet-the-team")
        assert self.driver.title == "Meet the Penn Cosmetic Surgery Team – Penn Cosmetics"

    def test_teampage(self):
        #asserting all doctors/headshots exist on the teampage
        assert self.driver.find_element(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_h2GroupTitle_0").text == "The Doctors"
        assert self.driver.find_element(By.CSS_SELECTOR, "#pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_0_divBio_0 .bio__name").text == "Joseph M. Serletti, MD, FACS"
        elements = self.driver.find_elements(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_0_imgHeadshot_0")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "#pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_1_divBio_1 .bio__name").text == "Ivona Percec, MD, PhD"
        elements = self.driver.find_elements(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_1_imgHeadshot_1")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "#pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_2_divBio_2 .bio__name").text == "Paris D. Butler, MD, MPH"
        elements = self.driver.find_elements(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_2_imgHeadshot_2")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "#pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_3_divBio_3 .bio__name").text == "Joshua Fosnot, MD"
        elements = self.driver.find_elements(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_3_imgHeadshot_3")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "#pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_4_divBio_4 .bio__name").text == "John Fischer, MD, MPH"
        elements = self.driver.find_elements(By.ID,"pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_4_imgHeadshot_4")
        assert len(elements) > 0

    def test_bioSerletti(self):
        self.driver.find_element(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_0_hypViewFullProfile_0").click()
        assert self.driver.title == "Joseph M. Serletti, MD, FACS – Penn Cosmetics"
        elements = self.driver.find_elements(By.ID, "pcmaincontent_0_imgHeadshot")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(6)").text == "Bringing creativity and collaboration to Penn Medicine"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".photo-right")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Contact Us"

    def test_viewProfLink(self):
        self.driver.find_element(By.ID, "pcmaincontent_0_rptTextHeadingsGroups_rptBio_0_personsListBioItem_0_hypViewFullProfile_0").click()
        self.driver.find_element(By.CSS_SELECTOR, "a > strong").click()
        assert self.driver.title == "Joseph M. Serletti, MD, FACS profile | PennMedicine.org"
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.CSS_SELECTOR, ".fad-h1").text == "Joseph M. Serletti, MD, FACS"


if __name__ == '__main__':
    unittest.main()
