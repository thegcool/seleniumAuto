import os
import configparser
# from config import*

class SystemProperties:
    # Required Variables
    JIRA_URL = ""
    RUNTIME_ENV = ""
    BUILD_ID = ""
    DRIVE_LOCATION = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config/config.ini")

        # Required Variables
        self.RUNTIME_ENV = os.environ.get("runtime.environment", "LOCAL")
        self.BUILD_ID = os.environ.get("BUILD_ID")
        self.DRIVE_LOCATION = os.environ["webdriver.chrome.driver"] = "path\\to\\chrome\\drive\\chromedriver.exe"
        # print(BUILD_ID)

        # These variables are required to run automation in remote server like docker.
        # self.REMOTE_DRIVER_URL = config.get("remote", "driver.url")
        # self.REMOTE_DRIVER_BROWSER_NAME = config.get("remote", "driver.browser.name", fallback="chrome")
        # self.REMOTE_DRIVER_BROWSER_VERSION = config.get("remote", "driver.browser.version", fallback="94.0")

        self.JIRA_URL = config.get("sd", "app.url")
    
