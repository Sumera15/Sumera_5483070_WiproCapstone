from behave import given, when, then

from pages.home_page import HomePage
from pages.saree_page import SareePage
from pages.checkout_page import CheckoutPage
from pages.women_page import WomenPage

from utils.logger import log_message
from utils.screenshot_util import take_screenshot


@given("User launches Myntra application")
def launch_app(context):

    context.home = HomePage(
        context.driver
    )

    context.home.open_myntra()

    log_message("Myntra opened")


@when("User hovers on Women section")
def women(context):

    context.home.hover_women()

    log_message("Hovered on Women section")


@when("User opens Fusion Wear page")
def fusion(context):

    context.women = WomenPage(
        context.driver
    )

    context.women.open_ethnic_wear()

    context.saree = SareePage(
        context.driver
    )

    assert "fusion-wear" in context.driver.current_url

    log_message("Fusion Wear page opened")

@when("User applies Sarees filter")
def saree_filter(context):

    context.saree.select_sarees_filter()

    log_message("Sarees filter selected")


@when("User selects Blue color filter")
def blue_filter(context):

    context.saree.select_blue_color()

    log_message("Blue color selected")


@when("User sorts products by Customer Rating")
def sort_rating(context):

    context.saree.sort_by_customer_rating()

    log_message("Customer rating selected")


@when("User selects first saree product")
def first_product(context):

    context.saree.select_first_product()

    context.checkout = CheckoutPage(
        context.driver
    )

    log_message("First product selected")


@when("User adds product to bag")
def add_bag(context):

    context.checkout.add_to_bag()

    log_message("Product added to bag")


@when("User opens bag page")
def bag(context):

    context.checkout.go_to_bag()

    log_message("Bag page opened")


@when("User increases quantity to 2")
def quantity(context):

    context.checkout.increase_quantity()

    context.checkout.select_quantity_two()

    log_message("Quantity increased to 2")


@when("User selects quantity Done button")
def done(context):

    context.checkout.click_done_button()

    log_message("Done button clicked")


@when("User selects donation amount")
def donation(context):

    context.checkout.select_donation_amount()

    log_message("Donation amount selected")


@when("User clicks Place Order")
def place_order(context):

    take_screenshot(
        context.driver,
        "Before_Place_Order"
    )

    context.checkout.click_place_order()

    log_message("Place order clicked")


@then("User should navigate to login page")
def login(context):

    assert "login" in context.driver.current_url.lower()

    take_screenshot(
        context.driver,
        "Login_Page"
    )

    log_message("Login page validated")