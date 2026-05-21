import os


if not os.path.exists("reports"):

    os.makedirs("reports")


if not os.path.exists("screenshots"):

    os.makedirs("screenshots")


if not os.path.exists("logs"):

    os.makedirs("logs")


os.system(
    "behave"
)

os.system(
    "allure generate reports -o allure-report --clean"
)

os.system(
    "allure open allure-report"
)