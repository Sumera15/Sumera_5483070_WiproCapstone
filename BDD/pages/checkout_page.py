from selenium.webdriver.common.by import By

from utils.waits import Waits

import time


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

    add_bag = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    bag = (
        By.XPATH,
        "//span[contains(text(),'Bag')]"
    )

    quantity = (
        By.XPATH,
        "//div[contains(@class,'itemComponents-base-quantity')]"
    )

    qty_two = (
        By.XPATH,
        "(//div[text()='2'])[1]"
    )

    done = (
        By.XPATH,
        "//div[contains(text(),'DONE')]"
    )

    donation = (
        By.XPATH,
        "//div[@data-key='20']"
    )

    place_order = (
        By.XPATH,
        "//div[contains(text(),'PLACE ORDER')]"
    )

    def add_to_bag(self):

        add = self.wait.wait_for_clickable(
            self.add_bag
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

        time.sleep(2)

    def go_to_bag(self):

        bag = self.wait.wait_for_clickable(
            self.bag
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bag
        )

        time.sleep(2)

    def increase_quantity(self):

        quantity = self.wait.wait_for_clickable(
            self.quantity
        )

        self.driver.execute_script(
            "arguments[0].click();",
            quantity
        )

        time.sleep(2)

    def select_quantity_two(self):

        qty = self.wait.wait_for_clickable(
            self.qty_two
        )

        self.driver.execute_script(
            "arguments[0].click();",
            qty
        )

        time.sleep(2)

    def click_done_button(self):

        done = self.wait.wait_for_clickable(
            self.done
        )

        self.driver.execute_script(
            "arguments[0].click();",
            done
        )

        time.sleep(2)

    def select_donation_amount(self):

        amount = self.wait.wait_for_clickable(
            self.donation
        )

        self.driver.execute_script(
            "arguments[0].click();",
            amount
        )

        time.sleep(2)

    def click_place_order(self):

        self.driver.execute_script(
            "window.scrollBy(0,500);"
        )

        time.sleep(2)

        order = self.wait.wait_for_clickable(
            self.place_order
        )

        self.driver.execute_script(
            "arguments[0].click();",
            order
        )

        time.sleep(3)