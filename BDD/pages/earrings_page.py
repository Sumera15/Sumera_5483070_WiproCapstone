from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import time


class EarringsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women = (
        By.XPATH,
        "//a[contains(text(),'Women')]"
    )

    earrings = (
        By.XPATH,
        "//a[contains(text(),'Earrings')]"
    )

    first_product = (
        By.XPATH,
        "(//img)[10]"
    )

    add_bag = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    def hover_women_and_open_earrings(self):

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

        earrings = self.wait.wait_for_clickable(
            self.earrings
        )

        actions.move_to_element(
            earrings
        ).perform()

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            earrings
        )

        time.sleep(3)

    def select_first_product(self):

        product = self.wait.wait_for_clickable(
            self.first_product
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(5)

        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    def add_to_bag(self):

        add = self.wait.wait_for_clickable(
            self.add_bag
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

        time.sleep(3)