from selenium.webdriver.common.by import By
import time


class CheckoutPage:

    def add_to_bag(self, driver):

        time.sleep(5)

        add_bag = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'ADD TO BAG')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            add_bag
        )

        time.sleep(5)

    def go_to_bag(self, driver):

        time.sleep(3)

        bag = driver.find_element(
            By.XPATH,
            "//span[contains(text(),'Bag')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            bag
        )

        time.sleep(5)

    def increase_quantity(self, driver):

        time.sleep(5)

        quantity = driver.find_element(
            By.XPATH,
            "//div[contains(@class,'itemComponents-base-quantity')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            quantity
        )

    def select_quantity_two(self, driver):

        time.sleep(3)

        qty_two = driver.find_element(
            By.XPATH,
            "(//div[text()='2'])[1]"
        )

        driver.execute_script(
            "arguments[0].click();",
            qty_two
        )

        time.sleep(3)

    def click_done_button(self, driver):

        time.sleep(2)

        done = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'DONE')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            done
        )

    def select_donation_amount(self, driver):

        time.sleep(5)

        amount = driver.find_element(
            By.XPATH,
            "//div[@data-key='20']"
        )

        driver.execute_script(
            "arguments[0].click();",
            amount
        )

    def click_place_order(self, driver):

        time.sleep(5)

        driver.execute_script(
            "window.scrollBy(0, 500);"
        )

        time.sleep(5)

        place_order = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'PLACE ORDER')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            place_order
        )