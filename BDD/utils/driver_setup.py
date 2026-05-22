from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import configparser


config = configparser.ConfigParser()

config.read("config/config.ini")


def get_driver():

    browser = config.get(
        "DEFAULT",
        "browser"
    )

    headless = config.getboolean(
        "DEFAULT",
        "headless"
    )

    implicit_wait = config.getint(
        "DEFAULT",
        "implicit_wait"
    )

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument(
        "--start-maximized"
    )

    chrome_options.add_argument(
        "--disable-notifications"
    )

    chrome_options.add_argument(
        "--disable-infobars"
    )

    chrome_options.add_argument(
        "--disable-extensions"
    )

    chrome_options.add_argument(
        "--disable-popup-blocking"
    )

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    if headless:

        chrome_options.add_argument(
            "--headless=new"
        )

    if browser.lower() == "chrome":

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=chrome_options
        )

        driver.implicitly_wait(
            implicit_wait
        )

        return driver