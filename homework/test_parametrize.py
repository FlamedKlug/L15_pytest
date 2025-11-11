"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s


@pytest.fixture(params=[300, 1080])
def browser_setup(request):
    if request.param == 300:
        browser.config.window_width = 300
    if request.param == 1080:
        browser.config.window_width = 1080
    browser.open("https://github.com/")

    yield
    browser.quit()


@pytest.mark.parametrize("browser_setup", [1080], indirect=True)
def test_github_desktop(browser_setup):
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))


@pytest.mark.parametrize("browser_setup", [300], indirect=True)
def test_github_mobile(browser_setup):
    s('.js-header-menu-toggle').click()
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))
