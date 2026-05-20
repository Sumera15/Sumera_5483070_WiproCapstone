import time

from pages.home_page import HomePage
from pages.kurti_page import KurtiPage
from pages.tshirt_page import TshirtPage
from pages.earrings_page import EarringsPage
from pages.flats_page import FlatsPage
from pages.size_validation_page import SizeValidationPage
from pages.pincode_validation_page import PincodeValidationPage

from utils.logger import log_message
from utils.screenshot_util import take_screenshot


def test_kurti_navigation():

    home = HomePage()

    kurti = KurtiPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    kurti.open_kurti(driver)

    log_message("Kurti page opened")

    assert "ethnic-tops" in driver.current_url.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()


def test_pink_tshirt_filter():

    home = HomePage()

    tshirt = TshirtPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    tshirt.hover_women_and_open_tshirt(driver)

    log_message("Tshirt page opened")

    tshirt.select_pink_color(driver)

    log_message("Pink color selected")

    tshirt.slow_scroll_down(driver)

    log_message("Slow scrolling completed")

    assert "tshirts" in driver.current_url.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()


def test_earrings_add_to_bag():

    home = HomePage()

    earrings = EarringsPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    earrings.hover_women_and_open_earrings(driver)

    log_message("Earrings page opened")

    earrings.select_first_product(driver)

    log_message("Earrings product selected")

    earrings.add_to_bag(driver)

    log_message("Product added to bag")

    assert "bag" in driver.page_source.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()


def test_flats_sorting():

    home = HomePage()

    flats = FlatsPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    flats.hover_women_and_open_flats(driver)

    log_message("Flats page opened")

    flats.sort_price_high_to_low(driver)

    log_message("Price High to Low selected")

    flats.slow_scroll_down(driver)

    log_message("Slow scrolling completed")

    assert "flats" in driver.current_url.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()


def test_size_validation():

    home = HomePage()

    size = SizeValidationPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    size.hover_women_and_open_tshirt(driver)

    log_message("Tshirt page opened")

    size.select_first_product(driver)

    log_message("Product selected")

    size.click_add_to_bag_without_size(driver)

    log_message("Add to bag clicked without size")

    assert "select" in driver.page_source.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()


def test_pincode_validation():

    home = HomePage()

    pincode = PincodeValidationPage()

    driver = home.open_myntra()

    log_message("Myntra opened")

    pincode.hover_women_and_open_heels(driver)

    log_message("Heels page opened")

    pincode.select_first_product(driver)

    log_message("Product selected")

    pincode.click_check_without_pincode(driver)

    log_message("Check clicked without entering pincode")

    assert "pincode" in driver.page_source.lower()

    take_screenshot(driver)

    time.sleep(5)

    driver.quit()