import time
import os
import allure


if not os.path.exists("screenshots"):

    os.makedirs("screenshots")


def take_screenshot(driver, name):

    timestamp = int(time.time())

    screenshot_path = (
        f"screenshots/{name}_{timestamp}.png"
    )

    driver.save_screenshot(screenshot_path)

    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=f"{name}_{timestamp}",
            attachment_type=allure.attachment_type.PNG
        )