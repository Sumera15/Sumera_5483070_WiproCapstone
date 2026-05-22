import pytest
from selenium import webdriver
import os


if not os.path.exists("reports"):

    os.makedirs("reports")


@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.myntra.com")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)