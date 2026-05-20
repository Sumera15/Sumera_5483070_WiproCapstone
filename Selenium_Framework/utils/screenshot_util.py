import time
import allure


def take_screenshot(driver):

    timestamp = int(time.time())

    screenshot_path = (
        f"screenshots/screenshot_{timestamp}.png"
    )

    driver.save_screenshot(screenshot_path)

    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=f"screenshot_{timestamp}",
            attachment_type=allure.attachment_type.PNG
        )