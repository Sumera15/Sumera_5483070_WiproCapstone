from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class Waits:

    def __init__(self, driver):

        self.driver = driver

    def wait_for_clickable(self, locator, time=15):

        return WebDriverWait(
            self.driver,
            time
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visible(self, locator, time=15):

        return WebDriverWait(
            self.driver,
            time
        ).until(
            EC.visibility_of_element_located(locator)
        )