from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class SareePage:

    def select_sarees_filter(self, driver):

        time.sleep(3)

        saree = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Sarees')]"
        )

        driver.execute_script(
            "arguments[0].click();",
            saree
        )

    def select_blue_color(self, driver):

        time.sleep(3)

        blue = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Blue')]"
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            blue
        )

        time.sleep(3)

        driver.execute_script(
            "arguments[0].click();",
            blue
        )

        time.sleep(5)

        driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    def sort_by_customer_rating(self, driver):

        time.sleep(3)

        sort = driver.find_element(
            By.XPATH,
            "//span[contains(text(),'Recommended')]"
        )

        sort.click()

        time.sleep(2)

        rating = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Customer Rating')]"
        )

        rating.click()

        time.sleep(5)

        driver.execute_script(
            "window.scrollBy(0, 600);"
        )

        time.sleep(5)

    def select_first_product(self, driver):

        time.sleep(5)

        product = driver.find_element(
            By.XPATH,
            "(//a[@target='_blank'])[3]"
        )

        driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(5)

        driver.switch_to.window(
            driver.window_handles[1]
        )