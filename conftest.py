import pytest
from selenium import webdriver
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if 'driver' in item.funcargs else 'w'
        try:
            web_driver = item.funcargs.get('driver')
            if web_driver:
                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f'Fail to take screenshot: {e}')