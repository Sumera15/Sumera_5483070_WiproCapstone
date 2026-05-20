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

    assert "Myntra" in driver.title

    log_message("Myntra opened")
    time.sleep(3)

    home.click_women(driver)
    log_message("Women section clicked")
    time.sleep(3)

    women.open_ethnic_wear(driver)

    assert "fusion-wear" in driver.current_url

    log_message("Ethnic wear page opened")
    time.sleep(3)

    saree.select_sarees_filter(driver)
    log_message("Sarees filter selected")
    time.sleep(3)

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
    time.sleep(3)

    checkout.go_to_bag(driver)

    assert "cart" in driver.current_url or "bag" in driver.current_url

    log_message("Bag page opened")
    time.sleep(3)

    checkout.increase_quantity(driver)
    log_message("Quantity dropdown opened")
    time.sleep(3)

    checkout.select_quantity_two(driver)
    log_message("Quantity changed to 2")
    time.sleep(3)

    checkout.click_done_button(driver)
    log_message("Done button clicked")
    time.sleep(3)

    checkout.select_donation_amount(driver)
    log_message("Donation amount selected")
    time.sleep(3)

    take_screenshot(driver)

    checkout.click_place_order(driver)

    assert "login" in driver.page_source.lower()

    log_message("Place order clicked")
    time.sleep(7)

    driver.quit()