from behave import given, when, then

from pages.end_to_end_page import EndToEndPage

from utils.logger import log_message
from utils.screenshot_util import take_screenshot


@given("User launches Myntra application")
def launch_app(context):

    context.e2e = EndToEndPage(
        context.driver
    )

    context.e2e.open_myntra()

    log_message(
        "Myntra application launched successfully"
    )


@when("User hovers on Women section")
def hover_women(context):

    context.e2e.hover_women_section()

    log_message(
        "Hovered on Women section successfully"
    )


@when("User opens Saree page")
def open_saree(context):

    context.e2e.open_saree_page()

    log_message(
        "Saree page opened successfully"
    )


@when("User selects Blue saree color")
def blue_filter(context):

    context.e2e.select_blue_color_filter()

    log_message(
        "Blue color filter selected successfully"
    )


@when("User selects first saree product")
def select_product(context):

    context.e2e.select_first_saree_product()

    log_message(
        "First saree product selected successfully"
    )


@when("User adds product to bag")
def add_bag(context):

    context.e2e.add_product_to_bag()

    log_message(
        "Product added to bag successfully"
    )


@when("User opens bag page")
def open_bag(context):

    context.e2e.open_bag_page()

    log_message(
        "Bag page opened successfully"
    )


@when("User increases quantity to 2")
def quantity(context):

    context.e2e.change_product_quantity()

    log_message(
        "Quantity updated to 2 successfully"
    )


@when("User clicks Place Order")
def place_order(context):

    take_screenshot(
        context.driver,
        "Before_Place_Order"
    )

    context.e2e.click_place_order()

    log_message(
        "Place Order button clicked successfully"
    )


@then("User should navigate to login page")
def login(context):

    context.e2e.validate_login_page()

    take_screenshot(
        context.driver,
        "Login_Page"
    )

    log_message(
        "Login page validated successfully"
    )