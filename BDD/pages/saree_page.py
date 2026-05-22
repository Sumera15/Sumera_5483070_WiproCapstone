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

    selected_blue_filter = (
        By.XPATH,
        "//span[contains(text(),'Blue')]"
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

        assert saree.is_displayed(), \
            "Sarees filter was not displayed"

        print("Sarees filter selected successfully")

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

        selected_blue = self.wait.wait_for_visible(
            self.selected_blue_filter
        )

        assert selected_blue.is_displayed(), \
            "Blue filter was not applied successfully"

        print("Blue filter applied successfully")

    def sort_by_customer_rating(self):

        sort = self.wait.wait_for_clickable(
            self.sort_dropdown
        )

        sort.click()

        rating = self.wait.wait_for_clickable(
            self.customer_rating
        )

        rating.click()

        assert rating.is_displayed(), \
            "Customer rating sort option not displayed"

        print("Sorted by customer rating successfully")

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

        assert len(
            self.driver.window_handles
        ) > 1, \
            "Product page did not open in new tab"

        print("First product selected successfully")