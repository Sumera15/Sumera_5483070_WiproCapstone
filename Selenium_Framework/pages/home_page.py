from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver


class HomePage:

    def open_myntra(self):

        driver = get_driver() #calls

        driver.get("https://www.myntra.com")

        return driver

    def click_women(self, driver):

        women = driver.find_element(By.LINK_TEXT, "Women")

        women.click()