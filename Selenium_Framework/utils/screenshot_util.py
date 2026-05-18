import time


def take_screenshot(driver):

    timestamp = int(time.time())

    driver.save_screenshot(
        f"screenshots/screenshot_{timestamp}.png"
    )