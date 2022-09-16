import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store')
    
    
@pytest.fixture(scope='session')
def browser(request):
    lang_val = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_val})
    browser = webdriver.Chrome(options=options)
    yield browser
