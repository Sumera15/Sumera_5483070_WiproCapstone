from behave import given, when, then

from pages.home_page import HomePage
from pages.kurti_page import KurtiPage
from pages.tshirt_page import TshirtPage
from pages.earrings_page import EarringsPage
from pages.flats_page import FlatsPage
from pages.size_validation_page import SizeValidationPage
from pages.pincode_validation_page import PincodeValidationPage

from utils.logger import log_message
from utils.screenshot_util import take_screenshot


@given("User opens Myntra website")
def open_myntra(context):

    context.home = HomePage(
        context.driver
    )

    context.home.open_myntra()

    log_message("Myntra opened")


# -----------------------------------
# KURTI NAVIGATION
# -----------------------------------

@when("User clicks on Women section")
def women(context):

    pass


@when("User opens Kurtis page")
def kurti(context):

    context.kurti = KurtiPage()

    context.kurti.open_kurti(
        context.driver
    )

    log_message("Kurti page opened")


@then("User should navigate to Kurtis page")
def verify_kurti(context):

    assert "ethnic-tops" in context.driver.current_url.lower()

    assert "women" in context.driver.title.lower()

    take_screenshot(
        context.driver,
        "Kurti_Page"
    )


# -----------------------------------
# PINK TSHIRT FILTER
# -----------------------------------

@when("User searches for Tshirts")
def tshirt(context):

    context.tshirt = TshirtPage()

    context.tshirt.hover_women_and_open_tshirt(
        context.driver
    )

    log_message("Tshirt page opened")


@when("User applies Pink color filter")
def pink(context):

    context.tshirt.select_pink_color(
        context.driver
    )

    context.tshirt.slow_scroll_down(
        context.driver
    )

    log_message("Pink filter applied")


@then("Pink Tshirts should display")
def verify_pink(context):

    assert "tshirts" in context.driver.current_url.lower()

    take_screenshot(
        context.driver,
        "Pink_Tshirt"
    )


# -----------------------------------
# EARRINGS ADD TO BAG
# -----------------------------------

@when("User searches for Earrings")
def earrings(context):

    context.earrings = EarringsPage()

    context.earrings.hover_women_and_open_earrings(
        context.driver
    )

    log_message("Earrings page opened")


@when("User selects first earrings product")
def earrings_product(context):

    context.earrings.select_first_product(
        context.driver
    )

    log_message("Earrings product selected")


@when("User adds earrings product to bag")
def add_earrings(context):

    context.earrings.add_to_bag(
        context.driver
    )

    log_message("Earrings added to bag")


@then("Earrings product should add successfully")
def verify_earrings(context):

    assert (
        "bag" in context.driver.page_source.lower()
        or
        "wishlist" in context.driver.page_source.lower()
    )

    take_screenshot(
        context.driver,
        "Earrings_Bag"
    )


# -----------------------------------
# FLATS SORTING
# -----------------------------------

@when("User searches for Flats")
def flats(context):

    context.flats = FlatsPage()

    context.flats.hover_women_and_open_flats(
        context.driver
    )

    log_message("Flats page opened")


@when("User sorts flats by Better Discount")
def flats_sort(context):

    context.flats.sort_price_high_to_low(
        context.driver
    )

    context.flats.slow_scroll_down(
        context.driver
    )

    log_message("Flats sorted")


@then("Flats products should display properly")
def verify_flats(context):

    assert "flats" in context.driver.current_url.lower()

    take_screenshot(
        context.driver,
        "Flats_Page"
    )


# -----------------------------------
# SIZE VALIDATION
# -----------------------------------

@when("User opens tshirt product")
def tshirt_product(context):

    context.size = SizeValidationPage()

    context.size.hover_women_and_open_tshirt(
        context.driver
    )

    context.size.select_first_product(
        context.driver
    )

    log_message("Tshirt product opened")


@when("User clicks Add to Bag without size")
def no_size(context):

    context.size.click_add_to_bag_without_size(
        context.driver
    )

    log_message("Clicked add to bag without size")


@then("User should see size validation message")
def size_validation(context):

    assert "size" in context.driver.page_source.lower()

    take_screenshot(
        context.driver,
        "Size_Validation"
    )


# -----------------------------------
# PINCODE VALIDATION
# -----------------------------------

@when("User enters invalid pincode")
def pincode(context):

    context.pincode = PincodeValidationPage()

    context.pincode.hover_women_and_open_heels(
        context.driver
    )

    context.pincode.select_first_product(
        context.driver
    )

    context.pincode.click_check_without_pincode(
        context.driver
    )

    log_message("Pincode validation checked")


@then("User should see invalid pincode validation")
def verify_pincode(context):

    assert "pincode" in context.driver.page_source.lower()

    take_screenshot(
        context.driver,
        "Pincode_Validation"
    )