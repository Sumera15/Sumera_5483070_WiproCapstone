import time

from pages.kurti_page import KurtiPage
from pages.tshirt_page import TshirtPage
from pages.earrings_page import EarringsPage
from pages.flats_page import FlatsPage
from pages.size_validation_page import SizeValidationPage
from pages.pincode_validation_page import PincodeValidationPage

from utils.logger import log_message
from utils.screenshot_util import take_screenshot


def test_kurti_navigation(driver):

    kurti = KurtiPage()

    log_message("Myntra opened")

    kurti.open_kurti(driver)

    log_message("Kurti page opened")

    take_screenshot(driver, "kurti_page_opened")

    assert "ethnic-tops" in driver.current_url.lower(), \
        "Kurti page did not open successfully"

    time.sleep(5)


def test_pink_tshirt_filter(driver):

    tshirt = TshirtPage()

    log_message("Myntra opened")

    tshirt.hover_women_and_open_tshirt(driver)

    log_message("Tshirt page opened")

    take_screenshot(driver, "tshirt_page_opened")

    tshirt.select_pink_color(driver)

    log_message("Pink color selected")

    take_screenshot(driver, "pink_color_selected")

    tshirt.slow_scroll_down(driver)

    log_message("Slow scrolling completed")

    take_screenshot(driver, "pink_tshirts_displayed")

    assert "tshirts" in driver.current_url.lower(), \
        "Tshirt page did not open successfully"

    time.sleep(5)


def test_earrings_add_to_bag(driver):

    earrings = EarringsPage()

    log_message("Myntra opened")

    earrings.hover_women_and_open_earrings(driver)

    log_message("Earrings page opened")

    take_screenshot(driver, "earrings_page_opened")

    earrings.select_first_product(driver)

    log_message("Earrings product selected")

    take_screenshot(driver, "earrings_product_selected")

    earrings.add_to_bag(driver)

    log_message("Product added to bag")

    take_screenshot(driver, "earrings_added_to_bag")

    assert "bag" in driver.page_source.lower(), \
        "Product was not added to bag"

    time.sleep(5)


def test_flats_sorting(driver):

    flats = FlatsPage()

    log_message("Myntra opened")

    flats.hover_women_and_open_flats(driver)

    log_message("Flats page opened")

    take_screenshot(driver, "flats_page_opened")

    flats.sort_price_high_to_low(driver)

    log_message("Price High to Low selected")

    take_screenshot(driver, "flats_sorted_high_to_low")

    flats.slow_scroll_down(driver)

    log_message("Slow scrolling completed")

    take_screenshot(driver, "flats_products_displayed")

    assert "flats" in driver.current_url.lower(), \
        "Flats page did not open successfully"

    time.sleep(5)


def test_size_validation(driver):

    size = SizeValidationPage()

    log_message("Myntra opened")

    size.hover_women_and_open_tshirt(driver)

    log_message("Tshirt page opened")

    take_screenshot(driver, "tshirt_page_opened")

    size.select_first_product(driver)

    log_message("Product selected")

    take_screenshot(driver, "tshirt_product_selected")

    size.click_add_to_bag_without_size(driver)

    log_message("Add to bag clicked without size")

    take_screenshot(driver, "size_validation_message")

    assert "select" in driver.page_source.lower(), \
        "Size validation message did not display"

    time.sleep(5)


def test_pincode_validation(driver):

    pincode = PincodeValidationPage()

    log_message("Myntra opened")

    pincode.hover_women_and_open_heels(driver)

    log_message("Heels page opened")

    take_screenshot(driver, "heels_page_opened")

    pincode.select_first_product(driver)

    log_message("Product selected")

    take_screenshot(driver, "heels_product_selected")

    pincode.click_check_without_pincode(driver)

    log_message("Check clicked without entering pincode")

    take_screenshot(driver, "pincode_validation_message")

    assert "pincode" in driver.page_source.lower(), \
        "Pincode validation message did not display"

    time.sleep(5)