from selenium import webdriver


driver = webdriver.Chrome(r"C:\Users\malin.nemergut\Desktop\Selenium\Selenium\PennCosmeticsLive\drivers\chromedriver.exe")


driver.get("https://google.com")
driver.quit()
