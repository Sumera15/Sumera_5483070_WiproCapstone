import os
import allure

from datetime import datetime


def take_screenshot(driver, name):

    if not os.path.exists("screenshots"):

        os.makedirs("screenshots")

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    screenshot_path = (
        f"screenshots/{name}_{timestamp}.png"
    )

    driver.save_screenshot(
        screenshot_path
    )

    allure.attach.file(
        screenshot_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )