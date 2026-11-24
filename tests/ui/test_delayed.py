
from playwright.sync_api import Page, expect

from tests.ui.pages.delayed_page import DelayedPage


def test_report_loads(page: Page):
    delayed = DelayedPage(page)
    delayed.open(delay_ms=2500)
    delayed.load_report()

    expect(delayed.report_status).to_have_text("Report ready")
    expect(delayed.report_table).to_be_visible()