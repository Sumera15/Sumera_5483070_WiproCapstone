from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import Waits

import configparser

import time


config = configparser.ConfigParser()

config.read(
    "config/config.ini"
)


class EndToEndPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = Waits(driver)

        self.base_url = config.get(
            "DEFAULT",
            "base_url"
        )

    women_menu = (
        By.LINK_TEXT,
        "WOMEN"
    )

    saree_menu = (
        By.XPATH,
        "//a[contains(@href,'saree')]"
    )

    blue_filter = (
        By.XPATH,
        "//label[contains(text(),'Blue')]"
    )

    selected_blue_filter = (
        By.XPATH,
        "//span[contains(text(),'Blue')]"
    )

    first_saree_product = (
        By.XPATH,
        "(//img[contains(@alt,'Saree')])[1]"
    )

    onesize_option = (
        By.XPATH,
        "//p[contains(text(),'Onesize')]"
    )

    add_to_bag_button = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    bag_button = (
        By.XPATH,
        "//span[contains(text(),'Bag')]"
    )

    quantity_dropdown = (
        By.XPATH,
        "//div[contains(@class,'itemComponents-base-dropDown')]"
    )

    quantity_two = (
        By.XPATH,
        "//div[@id='2']"
    )

    done_button = (
        By.XPATH,
        "//button[@role='button']"
    )

    donation_checkbox = (
        By.XPATH,
        "//input[@type='checkbox']"
    )

    donation_amount = (
        By.XPATH,
        "//div[@data-key='20']"
    )

    place_order_button = (
        By.XPATH,
        "//div[contains(text(),'PLACE ORDER')]"
    )

    login_validation = (
        By.XPATH,
        "//input[contains(@placeholder,'Mobile Number')]"
    )

    def open_myntra(self):

        self.driver.get(
            self.base_url
        )

        self.driver.maximize_window()

        assert "Myntra" in self.driver.title, \
            "Myntra homepage did not open"

    def hover_women_section(self):

        women = self.wait.wait_for_visible(
            self.women_menu
        )

        ActionChains(
            self.driver
        ).move_to_element(
            women
        ).perform()

        time.sleep(2)

    def open_saree_page(self):

        saree = self.wait.wait_for_clickable(
            self.saree_menu
        )

        self.driver.execute_script(
            "arguments[0].click();",
            saree
        )

        assert "saree" in self.driver.current_url.lower(), \
            "Saree page did not open"

    def select_blue_color_filter(self):

        blue = self.wait.wait_for_clickable(
            self.blue_filter
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            blue
        )

        self.driver.execute_script(
            "arguments[0].click();",
            blue
        )

        selected_blue = self.wait.wait_for_visible(
            self.selected_blue_filter
        )

        assert selected_blue.is_displayed(), \
            "Blue color filter was not selected"

    def select_first_saree_product(self):

        product = self.wait.wait_for_clickable(
            self.first_saree_product
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(5)

        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    def add_product_to_bag(self):

        try:

            onesize = self.wait.wait_for_clickable(
                self.onesize_option
            )

            self.driver.execute_script(
                "arguments[0].click();",
                onesize
            )

        except:

            pass

        add = self.wait.wait_for_clickable(
            self.add_to_bag_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

    def open_bag_page(self):

        bag = self.wait.wait_for_clickable(
            self.bag_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bag
        )

        assert (
            "bag" in self.driver.current_url.lower()
            or
            "cart" in self.driver.current_url.lower()
        ), "Bag page did not open"

    def change_product_quantity(self):

        quantity = self.wait.wait_for_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'itemComponents-base-quantity')]"
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            quantity
        )

        qty_two = self.wait.wait_for_clickable(
            (
                By.XPATH,
                "//div[@id='2']"
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            qty_two
        )

        done = self.wait.wait_for_clickable(
            (
                By.XPATH,
                "//button[@role='button']"
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            done
        )

        time.sleep(2)

        assert "Qty: 2" in self.driver.page_source, \
            "Quantity was not updated to 2"

    def select_donation_amount(self):

        self.driver.execute_script(
            "window.scrollBy(0, 700);"
        )

        time.sleep(3)

        donate = self.wait.wait_for_clickable(
            (
                By.XPATH,
                "//div[contains(text(),'Donate')]"
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            donate
        )

        time.sleep(2)

        amount = self.wait.wait_for_clickable(
            (
                By.XPATH,
                "//div[@data-key='20']"
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            amount
        )

        time.sleep(2)

        assert "20" in self.driver.page_source, \
            "Donation amount not selected"
    def click_place_order(self):

        self.driver.execute_script(
            "window.scrollBy(0,500);"
        )

        time.sleep(2)

        order = self.wait.wait_for_clickable(
            self.place_order_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            order
        )

    def validate_login_page(self):

        time.sleep(5)

        assert (
                "login" in self.driver.current_url.lower()
                or
                "login" in self.driver.page_source.lower()
        ), "Login page did not appear after clicking Place Order"