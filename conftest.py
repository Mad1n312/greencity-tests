import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")
    driver.maximize_window()
    yield driver

    driver.quit()