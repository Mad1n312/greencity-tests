from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    eco_news_link_locator = (
    By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Еко новини') or contains(., 'Eco news')]")
    events_link_locator = (
    By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    @allure.step("Клік на кнопку 'Sign In'")
    def click_sign_in(self):
        sign_in_button = self.get_sign_in_button()
        sign_in_button.click()

    def get_language_switcher(self):
        return self.driver.find_element(*self.language_switcher)

    @allure.step("Зміна мови інтерфейсу на: {language}")
    def switch_language(self, language):
        language_switcher = self.get_language_switcher()
        language_switcher.click()
        # self.wait.until(EC.element_to_be_clickable(self.language_switcher)).click()
        if language.lower() == "en":
            language_option = self.driver.find_element(*self.language_en_option)
        elif language.lower() == "uk":
            language_option = self.driver.find_element(*self.language_ua_option)
        else:
            raise ValueError("Unsupported language: {}".format(language))
        language_option.click()
        sleep(1)

    def get_eco_news_link(self):
        return self.driver.find_element(*self.eco_news_link_locator)

    @allure.step("Перехід на сторінку 'Eco News'")
    def navigate_to_eco_news(self):
        eco_news_link = self.get_eco_news_link()
        eco_news_link.click()

    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)

    @allure.step("Перехід на сторінку 'Events'")
    def navigate_to_events(self):
        events_link = self.get_events_link()
        events_link.click()

    @allure.step("Очікування видимості елемента")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
