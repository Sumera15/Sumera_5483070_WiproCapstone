from utils.driver_setup import get_driver
from utils.logger import log_message

import allure
import os
import configparser


config = configparser.ConfigParser()

config.read("config/config.ini")


def before_scenario(context, scenario):

    browser = config.get(
        "DEFAULT",
        "browser"
    )

    context.driver = get_driver()

    context.driver.implicitly_wait(
        int(
            config.get(
                "DEFAULT",
                "implicit_wait"
            )
        )
    )

    log_message(
        f"Starting Scenario: {scenario.name}"
    )

    log_message(
        f"Browser Used: {browser}"
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