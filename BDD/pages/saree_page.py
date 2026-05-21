from selenium.webdriver.common.by import By

from utils.waits import Waits

import time


class SareePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    saree_filter = (
        By.XPATH,
        "//label[contains(text(),'Sarees')]"
    )

    blue_filter = (
        By.XPATH,
        "//label[contains(text(),'Blue')]"
    )

    sort_dropdown = (
        By.XPATH,
        "//span[contains(text(),'Recommended')]"
    )

    customer_rating = (
        By.XPATH,
        "//label[contains(text(),'Customer Rating')]"
    )

    first_product = (
        By.XPATH,
        "(//a[@target='_blank'])[3]"
    )

    def select_sarees_filter(self):

        saree = self.wait.wait_for_clickable(
            self.saree_filter
        )

        self.driver.execute_script(
            "arguments[0].click();",
            saree
        )

    def select_blue_color(self):

        blue = self.wait.wait_for_clickable(
            self.blue_filter
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            blue
        )

        self.driver.execute_script(
            "arguments[0].click();",
            blue
        )

    def sort_by_customer_rating(self):

        sort = self.wait.wait_for_clickable(
            self.sort_dropdown
        )

        sort.click()

        rating = self.wait.wait_for_clickable(
            self.customer_rating
        )

        rating.click()

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