from playwright.sync_api import Page
BASE_URL = "https://rahulshettyacademy.com/AutomationPractice/"


def test_page_title(page: Page):
    page.goto(BASE_URL)
    title = page.title()
    assert "Practice Page" in title

def test_radio_button(page: Page):
    page.goto(BASE_URL)
    page.locator("input[value='radio2']").click()
    assert page.locator("input[value='radio2']").is_checked()

def test_checkbox(page: Page):
    page.goto(BASE_URL)
    checkbox = page.locator("#checkBoxOption1")
    checkbox.check()
    assert checkbox.is_checked()

def test_dropdown(page: Page):
    page.goto(BASE_URL)
    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option("option2")
    value = dropdown.input_value()
    assert value == "option2"

def test_switch_tab(page: Page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    # waiting for the new tab to open after clciking the button
    with page.context.expect_page() as new_page_event:
        page.locator("#opentab").click()
    new_tab = new_page_event.value
    # Wait for new tab to load
    new_tab.wait_for_load_state()
    # Validating an URL of new tab
    assert new_tab.url == "https://www.qaclickacademy.com/"
    # Validating a page title
    assert "QAClick Academy " in new_tab.title()