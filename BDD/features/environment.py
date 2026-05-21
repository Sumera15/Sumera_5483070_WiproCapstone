

from utils.driver_setup import get_driver
from utils.logger import log_message

import allure
import os


def before_scenario(context, scenario):

    context.driver = get_driver()

    log_message(
        f"Starting Scenario: {scenario.name}"
    )


def after_scenario(context, scenario):

    screenshot_name = scenario.name.replace(
        " ",
        "_"
    )

    screenshot_path = (
        f"screenshots/{screenshot_name}.png"
    )

    context.driver.save_screenshot(
        screenshot_path
    )

    allure.attach.file(
        screenshot_path,
        name="Scenario Screenshot",
        attachment_type=allure.attachment_type.PNG
    )

    log_message(
        f"Completed Scenario: {scenario.name}"
    )

    context.driver.quit()