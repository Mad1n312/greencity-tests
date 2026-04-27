

import re

from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.components.event_card_components import EventCardComponent
from selenium.webdriver.common.keys import Keys
class EventsPage(BasePage):

    main_header_locator = (By.XPATH, "//p[contains(@class, 'main-header')]")
    items_fount_locator = (By.XPATH, "//div[@class='active-filter-container']/p")
    cards_locator = (By.XPATH, "//mat-card")
    more_in_card_locator = (By.XPATH, ".//button[normalize-space()='More' or normalize-space()='Більше']")

    search_button_locator = (By.CSS_SELECTOR, "div.container-img.ng-star-inserted")
    search_input_locator = (By.CSS_SELECTOR, "input.place-input")
    status_filter_button = (By.ID, "mat-select-4")
    status_options = {
        "Відкритий": "mat-option-8",
        "Закритий": "mat-option-9",
        "Open": "mat-option-8",
        "Closed": "mat-option-9"
    }
    status_label_in_card = (By.CSS_SELECTOR, ".event-status")
    sign_in_form_locator = (By.CSS_SELECTOR, "form.sign-in-form")

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_header(self):
        return self.driver.find_element(*self.main_header_locator)
    def get_items_found(self):
        return self.driver.find_element(*self.items_fount_locator)
    
    def get_items_count(self):
        items_found = self.get_items_found()
        text = items_found.text

        match = re.search(r'\d+', text)
        if match:
            result = int(match.group())
            return result

    def get_cards(self)->list[EventCardComponent]:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.cards_locator)
            )
        except:
            return []

        cards_web_elements = self.driver.find_elements(*self.cards_locator)
        cards = []
        for card_element in cards_web_elements:
            card = EventCardComponent(card_element)
            cards.append(card)

        return cards

    def open_search(self):
        search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button_locator))
        search_btn.click()

    def fill_search_field(self, text):
        search_field = self.driver.find_element(*self.search_input_locator)
        search_field.clear()
        search_field.send_keys(text)


    def set_status_filter(self, status_name):
        """
        Метод перевіряє, чи відкрите меню,
        вибирає статус і закриває меню тільки в кінці.
        """
        # 1. Шукаємо оверлей списку (cdk-overlay-pane), який ми бачимо на скріншоті
        overlay = self.driver.find_elements(By.CSS_SELECTOR, ".cdk-overlay-pane")

        # Якщо список ще не відкритий (overlay порожній) — натискаємо на кнопку фільтра
        if not overlay:
            self.wait.until(EC.element_to_be_clickable(self.status_filter_button)).click()

        # 2. Отримуємо ID зі словника та клікаємо по опції
        option_id = self.status_options.get(status_name)
        self.wait.until(EC.element_to_be_clickable((By.ID, option_id))).click()


    def press_Escape(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

    def wait_until_status_applied(self, status_name):
        status_xpath = f"//div[contains(@class, 'event-status') and contains(text(), '{status_name}')]"
        return self.wait_for_element((By.XPATH, status_xpath))

    def is_login_form_displayed(self):
        return self.wait_for_element(self.sign_in_form_locator)

    def search_event_by_name(self, name):
        self.open_search()
        self.fill_search_field(name)

    def wait_for_page_to_load(self):
        return self.wait_for_element(self.main_header_locator)