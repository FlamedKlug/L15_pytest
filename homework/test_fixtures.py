"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser
import pytest
from selene.support.conditions import have
from selene.support.shared.jquery_style import s


@pytest.fixture()
def browser_setup_mobile():
    browser.config.window_width = 300
    browser.open("https://github.com/")

    yield
    browser.quit()


@pytest.fixture()
def browser_setup_desktop():
    browser.config.window_width = 1080
    browser.open("https://github.com/")

    yield
    browser.quit()


def test_github_desktop(browser_setup_desktop):
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))


def test_github_mobile(browser_setup_mobile):
    s('.js-header-menu-toggle').click()
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))
