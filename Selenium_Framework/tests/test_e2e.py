import time

from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.saree_page import SareePage
from pages.checkout_page import CheckoutPage
from utils.screenshot_util import take_screenshot
from utils.logger import log_message


def test_end_to_end_flow():

    home = HomePage()

    women = WomenPage()

    saree = SareePage()

    checkout = CheckoutPage()

    driver = home.open_myntra()
    log_message("Myntra opened")
    time.sleep(3)

    home.click_women(driver)
    log_message("Women section clicked")
    time.sleep(3)

    women.open_ethnic_wear(driver)
    log_message("Ethnic wear page opened")
    time.sleep(3)

    saree.select_sarees_filter(driver)
    log_message("Sarees filter selected")
    time.sleep(5)

    saree.select_blue_color(driver)
    log_message("Blue color selected")
    time.sleep(3)

    saree.sort_by_customer_rating(driver)
    log_message("Sorted by customer rating")
    time.sleep(3)

    saree.select_first_product(driver)
    log_message("Product added to bag")
    time.sleep(3)

    checkout.add_to_bag(driver)
    log_message("Product added to bag")
    time.sleep(5)

    checkout.go_to_bag(driver)
    log_message("Bag page opened")
    time.sleep(5)

    take_screenshot(driver)
    time.sleep(5)

    driver.quit()