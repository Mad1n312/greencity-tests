from src.pages.events_page import EventsPage
import allure
@allure.feature("Events Management")
@allure.story("Filter System")
def test_tc02_filter_status_cycle(driver):
    page = EventsPage(driver)
    page.wait_for_element(page.main_header_locator)
    page.switch_language("uk")

    page.set_status_filter("Відкритий")
    cards = page.get_cards()
    assert cards[0].get_status() == "Відкритий"

    page.set_status_filter("Відкритий")  # Знімаємо вибір
    page.set_status_filter("Закритий")  # Вибираємо новий
    page.press_escape()

    page.wait_until_status_applied("Закритий")
    cards = page.get_cards()
    assert cards[0].get_status() == "Закритий"