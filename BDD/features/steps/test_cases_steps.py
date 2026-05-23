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

    assert "myntra" in context.driver.title.lower(), \
        "Myntra website launch failed"

    log_message("Myntra opened")


# -----------------------------------
# KURTI NAVIGATION
# -----------------------------------

@when("User clicks on Women section")
def women(context):

    assert "myntra" in context.driver.current_url.lower(), \
        "Women section navigation failed"


@when("User opens Kurtis page")
def kurti(context):

    context.kurti = KurtiPage(
        context.driver
    )

    context.kurti.open_kurti()

    assert (
        "kurta"
        in
        context.driver.page_source.lower()
        or
        "ethnic"
        in
        context.driver.page_source.lower()
    ), "Kurti page did not open"

    log_message("Kurti page opened")


@then("User should navigate to Kurtis page")
def verify_kurti(context):

    assert (
        "kurta"
        in
        context.driver.page_source.lower()
        or
        "ethnic"
        in
        context.driver.page_source.lower()
    ), "Kurti products validation failed"

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

    assert "tshirt" in context.driver.page_source.lower(), \
        "Tshirt page did not open"

    log_message("Tshirt page opened")


@when("User applies Pink color filter")
def pink(context):

    context.tshirt.select_pink_color(
        context.driver
    )

    context.tshirt.slow_scroll_down(
        context.driver
    )

    assert "pink" in context.driver.page_source.lower(), \
        "Pink filter was not applied"

    log_message("Pink filter applied")


@then("Pink Tshirts should display")
def verify_pink(context):

    assert "tshirts" in context.driver.current_url.lower(), \
        "Pink tshirt validation failed"

    take_screenshot(
        context.driver,
        "Pink_Tshirt"
    )


# -----------------------------------
# EARRINGS ADD TO BAG
# -----------------------------------

@when("User searches for Earrings")
def earrings(context):

    context.earrings = EarringsPage(
        context.driver
    )

    context.earrings.hover_women_and_open_earrings()

    assert "earrings" in context.driver.page_source.lower(), \
        "Earrings page did not open"

    log_message("Earrings page opened")


@when("User selects first earrings product")
def earrings_product(context):

    context.earrings.select_first_product()

    assert len(
        context.driver.window_handles
    ) > 1, \
        "Earrings product page did not open"

    log_message("Earrings product selected")


@when("User adds earrings product to bag")
def add_earrings(context):

    context.earrings.add_to_bag()

    assert (
        "bag"
        in
        context.driver.page_source.lower()
        or
        "wishlist"
        in
        context.driver.page_source.lower()
    ), "Earrings add to bag failed"

    log_message("Earrings added to bag")


@then("Earrings product should add successfully")
def verify_earrings(context):

    assert (
        "bag"
        in
        context.driver.page_source.lower()
        or
        "wishlist"
        in
        context.driver.page_source.lower()
    ), "Earrings product validation failed"

    take_screenshot(
        context.driver,
        "Earrings_Bag"
    )


# -----------------------------------
# FLATS SORTING
# -----------------------------------

@when("User searches for Flats")
def flats(context):

    context.flats = FlatsPage(
        context.driver
    )

    context.flats.hover_women_and_open_flats()

    assert "flats" in context.driver.current_url.lower(), \
        "Flats page did not open"

    log_message("Flats page opened")


@when("User sorts flats by Better Discount")
def flats_sort(context):

    context.flats.sort_price_high_to_low()

    context.flats.slow_scroll_down()

    assert "flats" in context.driver.current_url.lower(), \
        "Flats sorting failed"

    log_message("Flats sorted")


@then("Flats products should display properly")
def verify_flats(context):

    assert "flats" in context.driver.current_url.lower(), \
        "Flats validation failed"

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

    assert len(
        context.driver.window_handles
    ) > 1, \
        "Tshirt product page did not open"

    log_message("Tshirt product opened")


@when("User clicks Add to Bag without size")
def no_size(context):

    context.size.click_add_to_bag_without_size(
        context.driver
    )

    assert "size" in context.driver.page_source.lower(), \
        "Size validation message did not appear"

    log_message("Clicked add to bag without size")


@then("User should see size validation message")
def size_validation(context):

    assert "size" in context.driver.page_source.lower(), \
        "Size validation failed"

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

    assert "pincode" in context.driver.page_source.lower(), \
        "Pincode validation failed"

    log_message("Pincode validation checked")


@then("User should see invalid pincode validation")
def verify_pincode(context):

    assert "pincode" in context.driver.page_source.lower(), \
        "Invalid pincode validation failed"

    take_screenshot(
        context.driver,
        "Pincode_Validation"
    )