from src.pages.events_page import EventsPage


def test_tc01_search_by_name(driver):
    page = EventsPage(driver)
    page.navigate_to_events()
    page.wait_for_page_to_load()

    target_name = "TESTEVENT"
    page.search_event_by_name(target_name)

    cards = page.get_cards()
    assert len(cards) > 0, f"Event with name '{target_name}' was not found!"

    assert target_name in cards[0].get_name(), f"Expected '{target_name}', but got '{cards[0].get_name()}'"

