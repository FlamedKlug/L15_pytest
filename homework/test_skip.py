"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
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


def test_github_desktop(browser_setup):
    if browser.config.window_width == 300:
        pytest.skip(reason="В десктопном тесте не запускаем браузер с шириной 300")
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))


def test_github_mobile(browser_setup):
    if browser.config.window_width == 1080:
        pytest.skip(reason="В мобильном тесте не запускаем браузер с шириной 1080")
    s('.js-header-menu-toggle').click()
    s('.HeaderMenu-link--sign-up').click()
    s('#signup-form-fields').should(have.text("Sign up for GitHub"))
