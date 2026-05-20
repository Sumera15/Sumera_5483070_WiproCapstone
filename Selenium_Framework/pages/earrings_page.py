from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class EarringsPage:

    def hover_women_and_open_earrings(self, driver):

        time.sleep(3)

        women = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Women')]"
        )

        actions = ActionChains(driver)

        actions.move_to_element(women).perform()

        time.sleep(3)

        earrings = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Earrings')]"
        )

        actions.move_to_element(earrings).perform()

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            earrings
        )

        time.sleep(5)

    def select_first_product(self, driver):

        time.sleep(5)

        product = driver.find_element(
            By.XPATH,
            "(//img)[10]"
        )

        driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(5)

        driver.switch_to.window(
            driver.window_handles[1]
        )

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