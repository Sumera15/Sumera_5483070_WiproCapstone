import time
import pytest

from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.saree_page import SareePage
from pages.checkout_page import CheckoutPage

from utils.screenshot_util import take_screenshot
from utils.logger import log_message


@pytest.mark.parametrize(
    "color",
    ["Blue"]
)
def test_end_to_end_flow(driver, color):

    home = HomePage()

    women = WomenPage()

    saree = SareePage()

    checkout = CheckoutPage()

    assert "Myntra" in driver.title, \
        "Myntra homepage did not open successfully"

    log_message("Myntra opened")

    take_screenshot(driver, "myntra_homepage")

    time.sleep(3)

    home.click_women(driver)

    log_message("Women section clicked")

    take_screenshot(driver, "women_section_opened")

    time.sleep(3)

    women.open_ethnic_wear(driver)

    assert "fusion-wear" in driver.current_url, \
        "Fusion wear page did not open successfully"

    log_message("Ethnic wear page opened")

    take_screenshot(driver, "fusion_wear_page_opened")

    time.sleep(3)

    saree.select_sarees_filter(driver)

    log_message("Sarees filter selected")

    take_screenshot(driver, "sarees_filter_selected")

    time.sleep(3)

    if color == "Blue":

        saree.select_blue_color(driver)

        log_message("Blue color selected")

        take_screenshot(driver, "blue_color_selected")

    time.sleep(3)

    saree.sort_by_customer_rating(driver)

    log_message("Sorted by customer rating")

    take_screenshot(driver, "sorted_by_customer_rating")

    time.sleep(3)

    saree.select_first_product(driver)

    log_message("Product selected")

    take_screenshot(driver, "saree_product_selected")

    time.sleep(3)

    checkout.add_to_bag(driver)

    log_message("Product added to bag")

    take_screenshot(driver, "product_added_to_bag")

    time.sleep(3)

    checkout.go_to_bag(driver)

    assert "cart" in driver.current_url.lower() or \
           "bag" in driver.current_url.lower(), \
           "Bag page did not open successfully"

    log_message("Bag page opened")

    take_screenshot(driver, "bag_page_opened")

    time.sleep(3)

    checkout.increase_quantity(driver)

    log_message("Quantity dropdown opened")

    take_screenshot(driver, "quantity_dropdown_opened")

    time.sleep(3)

    checkout.select_quantity_two(driver)

    log_message("Quantity changed to 2")

    take_screenshot(driver, "quantity_changed_to_2")

    time.sleep(3)

    checkout.click_done_button(driver)

    log_message("Done button clicked")

    take_screenshot(driver, "done_button_clicked")

    time.sleep(3)

    checkout.select_donation_amount(driver)

    log_message("Donation amount selected")

    take_screenshot(driver, "donation_amount_selected")

    time.sleep(3)

    checkout.click_place_order(driver)

    assert "login" in driver.page_source.lower(), \
        "Login page did not display"

    log_message("Place order clicked")

    take_screenshot(driver, "login_page_displayed")

    time.sleep(7)