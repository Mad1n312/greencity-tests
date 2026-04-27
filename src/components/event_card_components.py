
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class EventCardComponent(BaseComponent):
    more_button_locator = (By.XPATH, "./app-events-list-item/div/div[3]/div[2]/button[1]")
    name_locator = (By.XPATH, ".//p[contains(@class, 'event-name')]")
    status_locator = (By.CSS_SELECTOR, ".event-status")
    join_button_locator = (By.CSS_SELECTOR, ".primary-global-button.event-button")

    def click_more(self):
        more_button = self.find_element(*self.more_button_locator)
        more_button.click()

    def click_join(self):
        btn = self.node.find_element(*self.join_button_locator)
        btn.click()

    def get_name(self):
        name_element = self.find_element(*self.name_locator)
        return name_element.text

    def get_status(self):
        status_element = self.node.find_element(*self.status_locator)
        return status_element.text.strip()

