from selenium.webdriver.common.by import By

from utils.waits import Waits


class WomenPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    ethnic_wear = (
        By.XPATH,
        "//a[contains(text(),'Ethnic Wear')]"
    )

    def open_ethnic_wear(self):

        ethnic = self.wait.wait_for_clickable(
            self.ethnic_wear
        )

        self.driver.execute_script(
            "arguments[0].click();",
            ethnic
        )