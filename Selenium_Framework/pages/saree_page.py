from selenium.webdriver.common.by import By
import time


class SareePage:

    def select_sarees_filter(self, driver):

        time.sleep(3)

        saree = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Sarees')]"
        )

        driver.execute_script("arguments[0].click();", saree) #Execute JavaScript click on saree element

    def select_blue_color(self, driver):

        time.sleep(3)

        blue = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Blue')]"
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", blue)

        time.sleep(3)

        driver.execute_script("arguments[0].click();", blue)

        time.sleep(5)

        driver.execute_script("window.scrollTo(0, 0);")

    def sort_by_customer_rating(self, driver):

        time.sleep(3)

        sort = driver.find_element(
            By.XPATH,
            "//div[contains(text(),'Sort by')]"
        )

        driver.execute_script("arguments[0].click();", sort)

        time.sleep(2)

        rating = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Customer Rating')]"
        )

        driver.execute_script("arguments[0].click();", rating)

    def select_first_product(self, driver):

        time.sleep(5)

        product = driver.find_element(
            By.XPATH,
            "(//img[@class='img-responsive'])[1]"
        )

        driver.execute_script("arguments[0].click();", product)