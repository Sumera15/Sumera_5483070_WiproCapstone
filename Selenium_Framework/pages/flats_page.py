from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class FlatsPage:

    def hover_women_and_open_flats(self, driver):

        time.sleep(3)

        women = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Women')]"
        )

        actions = ActionChains(driver)

        actions.move_to_element(women).perform()

        time.sleep(3)

        flats = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Flats')]"
        )

        actions.move_to_element(flats).perform()

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            flats
        )

        time.sleep(5)

    def sort_price_high_to_low(self, driver):

        time.sleep(3)

        current_sort = driver.find_element(
            By.XPATH,
            "//div[@class='sort-sortBy']"
        ).text

        if "Price: High To Low" in current_sort:

            print("Already sorted")

        else:

            sort = driver.find_element(
                By.XPATH,
                "//div[@class='sort-sortBy']"
            )

            driver.execute_script(
                "arguments[0].click();",
                sort
            )

            time.sleep(3)

            high_to_low = driver.find_element(
                By.XPATH,
                "//label[contains(text(),'Price: High to Low')]"
            )

            driver.execute_script(
                "arguments[0].click();",
                high_to_low
            )

            time.sleep(5)

    def slow_scroll_down(self, driver):

        for i in range(8):

            driver.execute_script(
                "window.scrollBy(0, 500);"
            )

            time.sleep(2)