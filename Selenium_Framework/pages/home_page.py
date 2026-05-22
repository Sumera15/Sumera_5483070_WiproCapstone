from selenium.webdriver.common.by import By


class HomePage:

    def click_women(self, driver):

        women = driver.find_element(
            By.LINK_TEXT,
            "Women"
        )

        women.click()