from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import time


class FlatsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women = (
        By.XPATH,
        "//a[contains(text(),'Women')]"
    )

    flats = (
        By.XPATH,
        "//a[contains(text(),'Flats')]"
    )

    sort_dropdown = (
        By.XPATH,
        "//div[@class='sort-sortBy']"
    )

    high_to_low = (
        By.XPATH,
        "//label[contains(text(),'Price: High to Low')]"
    )

    def hover_women_and_open_flats(self):

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

        flats = self.wait.wait_for_clickable(
            self.flats
        )

        actions.move_to_element(
            flats
        ).perform()

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            flats
        )

        time.sleep(3)

    def sort_price_high_to_low(self):

        current_sort = self.wait.wait_for_visible(
            self.sort_dropdown
        ).text

        if "Price: High To Low" in current_sort:

            print("Already sorted")

        else:

            sort = self.wait.wait_for_clickable(
                self.sort_dropdown
            )

            self.driver.execute_script(
                "arguments[0].click();",
                sort
            )

            time.sleep(2)

            high = self.wait.wait_for_clickable(
                self.high_to_low
            )

            self.driver.execute_script(
                "arguments[0].click();",
                high
            )

            time.sleep(3)

    def slow_scroll_down(self):

        for i in range(8):

            self.driver.execute_script(
                "window.scrollBy(0,500);"
            )

            time.sleep(1)