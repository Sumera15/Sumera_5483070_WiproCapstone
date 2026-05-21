from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import time


class KurtiPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women = (
        By.XPATH,
        "//a[contains(text(),'Women')]"
    )

    kurti = (
        By.XPATH,
        "//a[contains(text(),'Kurtis, Tunics & Tops')]"
    )

    def open_kurti(self):

        women = self.wait.wait_for_visible(
            self.women
        )

        actions = ActionChains(
            self.driver
        )

        actions.move_to_element(
            women
        ).perform()

        time.sleep(2)

        kurti = self.wait.wait_for_clickable(
            self.kurti
        )

        actions.move_to_element(
            kurti
        ).perform()

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            kurti
        )

        time.sleep(3)