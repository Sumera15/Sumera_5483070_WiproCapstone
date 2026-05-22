from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import time


class WomenPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women = (
        By.XPATH,
        "//a[contains(text(),'Women')]"
    )

    ethnic_wear = (
        By.XPATH,
        "//a[contains(@href,'fusion-wear')]"
    )

    def open_ethnic_wear(self):

        women = self.wait.wait_for_visible(
            self.women
        )

        ActionChains(
            self.driver
        ).move_to_element(
            women
        ).perform()

        time.sleep(3)

        ethnic = self.wait.wait_for_clickable(
            self.ethnic_wear
        )

        self.driver.execute_script(
            "arguments[0].click();",
            ethnic
        )

        time.sleep(3)