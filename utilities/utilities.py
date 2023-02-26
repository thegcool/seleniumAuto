import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from utilities.systemproperties import*

# Define a constant variable
CHROMEDRIVER_PATH = os.path.join('Z:', os.sep, 'OPSQC', 'Selenium', 'chromedriver.exe')


def delay(ms):
    time.sleep(ms / 1000)


def get_remote_webdriver(test_name):
    driver = None
    sdf = time.strftime('%m%d%Y%H%M%S')
    try:
        browser = DesiredCapabilities.CHROME.copy()
        browser['enableVNC'] = True
        browser['screenResolution'] = '1920x1080x24'
        browser['enableVideo'] = True
        browser['videoScreenSize'] = '1920x1080'
        browser['videoName'] = f"{systemproperties.BUILD_ID}-{test_name}-{sdf}.mp4"
        browser['enableLog'] = True
        browser['acceptInsecureCerts'] = True

        driver = webdriver.Remote(
            command_executor=systemproperties.JIRA_DEMO_URL,
            desired_capabilities=browser
        )
        driver.maximize_window()
    except Exception as e:
        print(e)
    return driver


def get_local_webdriver():
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            options=chrome_options
        )
        driver.maximize_window()
    except Exception as e:
        print(e)
    return driver


def browser_tab_exists(driver, url):
    for handle in driver.window_handles:
        delay(1000)
        driver.switch_to.window(handle)
        delay(1000)
        if url in driver.current_url:
            return True
    return False


def get_webdriver(test_name):
    driver = None
    if systemproperties.RUNTIME_ENV == 'LOCAL':
        driver = get_local_webdriver()
    else:
        driver = get_remote_webdriver(test_name)
    return driver
