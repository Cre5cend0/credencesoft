from selenium import webdriver
from utilities.config import MetaData
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests


# Setting up soup object for a given URL
def setup_bs(url):
    """
    requires one parameter: a webpage url -> str
    returns soup object
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS Catalina 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.69 Safari/537.36 '
    }
    # creating a html response object
    response = requests.get(url, headers=headers)

    # using lxml parser for maximum speed and compatibility (as recommended by the documentation)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


# Setting up Selenium driver object for a browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # to run without invoking the browser


def setup_selenium_driver(browser="chrome"):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=MetaData.CHROME)
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=MetaData.FIREFOX)
    if browser == 'safari':
        driver = webdriver.Safari(executable_path=MetaData.SAFARI)

    return driver
