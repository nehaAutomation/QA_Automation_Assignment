import pytest
from ui.pages.practice_page import PracticePage
from utils.config import BASE_UI_URL


@pytest.fixture
def practice_page(page):
    page.goto(BASE_UI_URL)
    return PracticePage(page)