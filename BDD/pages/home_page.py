from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women = (
        By.LINK_TEXT,
        "Women"
    )

    def open_myntra(self):
        self.driver.get(
            "https://www.myntra.com"
        )

        self.driver.maximize_window()

        
    def hover_women(self):

        women = self.wait.wait_for_visible(
            self.women
        )

        ActionChains(self.driver).move_to_element(
            women
        ).perform()

