from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class KurtiPage:

    def open_kurti(self, driver):

        time.sleep(3)

        women = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Women')]"
        )

        actions = ActionChains(driver)

        actions.move_to_element(women).perform()

        time.sleep(3)

        kurti = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Kurtis, Tunics & Tops')]"
        )

        actions.move_to_element(kurti).perform()

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            kurti
        )

        time.sleep(5)