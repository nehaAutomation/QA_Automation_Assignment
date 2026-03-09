from ui.pages.practice_page import PracticePage
from utils.config import BASE_UI_URL
from utils.logger import get_logger

logger = get_logger(__name__)


def test_page_title(practice_page):
    logger.info("Starting test: test_page_title")
    title = practice_page.get_title()
    logger.info(f"Page title is: {title}")
    assert "Practice Page" in title
    logger.info("test_page_title passed")


def test_radio_button(practice_page):
    logger.info("Starting test: test_radio_button")
    practice_page.click_radio2()
    logger.info("Clicked radio button 2")
    assert practice_page.radio2_checked()
    logger.info("Radio button verified as selected")


def test_checkbox(practice_page):
    logger.info("Starting test: test_checkbox")
    result = practice_page.check_checkbox1()
    logger.info("Checkbox option 1 selected")
    assert result
    logger.info("Checkbox verification passed")


def test_dropdown(practice_page):
    logger.info("Starting test: test_dropdown")
    value = practice_page.select_dropdown_option("option2")
    logger.info(f"Dropdown value selected: {value}")
    assert value == "option2"
    logger.info("Dropdown verification passed")


def test_switch_tab(practice_page):
    logger.info("Starting test: test_switch_tab")
    new_tab = practice_page.open_new_tab()
    logger.info("New tab opened")
    new_tab.wait_for_load_state()
    logger.info(f"New tab URL: {new_tab.url}")
    assert "qaclickacademy" in new_tab.url
    logger.info("Switch tab verification passed")