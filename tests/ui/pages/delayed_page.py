from playwright.sync_api import Page


class DelayedPage:
    def __init__(self, page: Page):
        self.page = page
        self.load_report_button = page.get_by_role("button", name="Load report")
        self.report_status = page.get_by_test_id("report-status")
        self.report_table = page.get_by_role("table")

    def open(self, delay_ms=None):
        # The page can use a fixed delay instead of a random one, for example ?delay=2500
        if delay_ms is None:
            self.page.goto("/playground/delayed")
        else:
            self.page.goto(f"/playground/delayed?delay={delay_ms}")

    def load_report(self):
        self.load_report_button.click()
