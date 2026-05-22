from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class PincodeValidationPage:

    def hover_women_and_open_heels(self, driver):

        time.sleep(3)

        women = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Women')]"
        )

        actions = ActionChains(driver)

        actions.move_to_element(women).perform()

        time.sleep(3)

        heels = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Heels')]"
        )

        actions.move_to_element(heels).perform()

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            heels
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

    def click_check_without_pincode(self, driver):

        time.sleep(5)

        driver.execute_script(
            "window.scrollBy(0, 500);"
        )

        time.sleep(3)

        pincode_box = driver.find_element(
            By.XPATH,
            "//input[@placeholder='Enter pincode']"
        )

        pincode_box.click()

        time.sleep(2)

        check = driver.find_element(
            By.XPATH,
            "//input[@value='Check']"
        )

        check.click()

        time.sleep(5)