class PracticePage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.radio2 = "input[value='radio2']"
        self.checkbox1 = "#checkBoxOption1"
        self.dropdown = "#dropdown-class-example"
        self.open_tab_button = "#opentab"

    # Page actions
    def get_title(self):
        return self.page.title()

    def click_radio2(self):
        self.page.locator(self.radio2).click()

    def radio2_checked(self):
        return self.page.locator(self.radio2).is_checked()

    def check_checkbox1(self):
        checkbox = self.page.locator(self.checkbox1)
        checkbox.check()
        return checkbox.is_checked()

    def select_dropdown_option(self, option):
        dropdown = self.page.locator(self.dropdown)
        dropdown.select_option(option)
        return dropdown.input_value()

    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_event:
            self.page.locator(self.open_tab_button).click()

        new_tab = new_page_event.value
        # Wait until navigation stabilizes
        new_tab.wait_for_load_state("domcontentloaded")
        return new_tab