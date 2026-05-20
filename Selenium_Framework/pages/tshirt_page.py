from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TshirtPage:

    def hover_women_and_open_tshirt(self, driver):

        time.sleep(3)

        women = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Women')]"
        )

        actions = ActionChains(driver)

        actions.move_to_element(women).perform()

        time.sleep(3)

        tshirt = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Tshirts')]"
        )

        actions.move_to_element(tshirt).perform()

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            tshirt
        )

        time.sleep(5)

    def select_pink_color(self, driver):

        time.sleep(5)

        driver.execute_script(
            "window.scrollBy(0, 500);"
        )

        time.sleep(3)

        pink = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Pink')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            pink
        )

        time.sleep(5)

    def slow_scroll_down(self, driver):

        for i in range(5):

            driver.execute_script(
                "window.scrollBy(0, 400);"
            )

            time.sleep(2)