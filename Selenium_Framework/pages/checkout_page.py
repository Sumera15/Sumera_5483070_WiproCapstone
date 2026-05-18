from selenium.webdriver.common.by import By
import time


class CheckoutPage:

    def add_to_bag(self, driver):

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        add_bag = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'ADD TO BAG')]"
        )

        driver.execute_script("arguments[0].click();", add_bag)

    def go_to_bag(self, driver):

        time.sleep(3)

        bag = driver.find_element(
            By.XPATH,
            "//span[contains(text(),'GO TO BAG')]"
        )

        driver.execute_script("arguments[0].click();", bag)