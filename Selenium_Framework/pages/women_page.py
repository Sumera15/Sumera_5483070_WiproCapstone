from selenium.webdriver.common.by import By
import time


class WomenPage:

    def open_ethnic_wear(self, driver):

        time.sleep(3)

        driver.execute_script(
            "window.scrollBy(0, 700);"
        )

        time.sleep(3)

        driver.get(
            "https://www.myntra.com/fusion-wear"
        )