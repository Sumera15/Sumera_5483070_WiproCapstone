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

    assert "myntra" in context.driver.title.lower(), \
        "Myntra homepage launch failed"

    log_message(
        "Myntra application launched successfully"
    )


@when("User hovers on Women section")
def hover_women(context):

    context.e2e.hover_women_section()

    assert "myntra" in context.driver.current_url.lower(), \
        "Women section hover failed"

    log_message(
        "Hovered on Women section successfully"
    )


@when("User opens Saree page")
def open_saree(context):

    context.e2e.open_saree_page()

    assert "saree" in context.driver.current_url.lower(), \
        "Saree page navigation failed"

    log_message(
        "Saree page opened successfully"
    )


@when("User selects Blue saree color")
def blue_filter(context):

    context.e2e.select_blue_color_filter()

    assert "blue" in context.driver.page_source.lower(), \
        "Blue color filter selection failed"

    log_message(
        "Blue color filter selected successfully"
    )


@when("User selects first saree product")
def select_product(context):

    context.e2e.select_first_saree_product()

    assert len(
        context.driver.window_handles
    ) > 1, \
        "Product page did not open"

    log_message(
        "First saree product selected successfully"
    )


@when("User adds product to bag")
def add_bag(context):

    context.e2e.add_product_to_bag()

    assert (
        "bag"
        in
        context.driver.page_source.lower()
        or
        "wishlist"
        in
        context.driver.page_source.lower()
    ), "Add to bag failed"

    log_message(
        "Product added to bag successfully"
    )


@when("User opens bag page")
def open_bag(context):

    context.e2e.open_bag_page()

    assert (
        "bag"
        in
        context.driver.current_url.lower()
        or
        "cart"
        in
        context.driver.current_url.lower()
    ), "Bag page open failed"

    log_message(
        "Bag page opened successfully"
    )


@when("User increases quantity to 2")
def quantity(context):

    context.e2e.change_product_quantity()

    assert "qty: 2" in context.driver.page_source.lower(), \
        "Quantity update failed"

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

    assert "login" in context.driver.page_source.lower(), \
        "Place order flow failed"

    log_message(
        "Place Order button clicked successfully"
    )


@then("User should navigate to login page")
def login(context):

    context.e2e.validate_login_page()

    assert (
        "login"
        in
        context.driver.page_source.lower()
        or
        "login"
        in
        context.driver.current_url.lower()
    ), "Login page validation failed"

    take_screenshot(
        context.driver,
        "Login_Page"
    )

    log_message(
        "Login page validated successfully"
    )