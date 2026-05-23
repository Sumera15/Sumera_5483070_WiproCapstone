from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import time


class FlatsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    women_menu = (
        By.LINK_TEXT,
        "WOMEN"
    )

    flats_menu = (
        By.XPATH,
        "//a[contains(text(),'Flats')]"
    )

    def hover_women_and_open_flats(self):

        women = self.wait.wait_for_visible(
            self.women_menu
        )

        ActionChains(
            self.driver
        ).move_to_element(
            women
        ).perform()

        time.sleep(2)

        flats = self.wait.wait_for_clickable(
            self.flats_menu
        )

        self.driver.execute_script(
            "arguments[0].click();",
            flats
        )

        time.sleep(3)

    def sort_price_high_to_low(self):

        time.sleep(3)

        assert (
            "flats"
            in
            self.driver.current_url.lower()
        ), "Flats page did not open"

    def slow_scroll_down(self):

        for i in range(5):

            self.driver.execute_script(
                "window.scrollBy(0,500);"
            )

            time.sleep(2)