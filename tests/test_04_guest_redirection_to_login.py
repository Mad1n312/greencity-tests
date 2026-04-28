from src.pages.events_page import EventsPage
import allure
@allure.feature("User Security")
@allure.story("Unauthorized Access Redirect")
def test_tc04_guest_redirection_to_login(driver):
    page = EventsPage(driver)
    page.wait_for_page_to_load()
    cards = page.get_cards()
    assert len(cards) > 0, "No event cards found on the page!"
    cards[0].click_join()
    assert page.is_login_form_displayed(), "Sign-in form is not visible after clicking Join"