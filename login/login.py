import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login.keyvalues import *
from jira_workhours.loghours import GetWorkHrs
from utilities.systemproperties import SystemProperties


class LoginScripts:
    def __init__(self, driver, wait, projectid):
        self.getworkhrs = None
        self.issue_actions_container = None
        self.driver = driver
        self.wait = wait
        self.sys_prop = SystemProperties()
        self.projectid = projectid

    def sign_in(self):
        expected_url = self.sys_prop.JIRA_URL + self.projectid
        print(expected_url)
        # assert expected_url in self.driver.current_url, "Expected to be in Jira login page"
        self.driver.get(expected_url)
        username = os.getenv('jirauser')
        password = os.getenv('jirapassword')
        self.get_username().send_keys(username)
        self.get_password_field().send_keys(password)
        self.get_login_button().click()
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(EC.visibility_of_element_located(JIRA_WORKLOGTAB))
            self.get_worklog_tab().click()
            self.issue_actions_container = self.get_log_div()
            print("this is good")
            print(self.issue_actions_container)
            self.getworkhours = GetWorkHrs(self.driver, self.wait, self.issue_actions_container)

            # work_hrs.get_work_hrs(issue_actions_container)
        except Exception as e:
            # print("Username or Password does not match.")
            print(e)
        return self

    def get_username(self):
        return self.driver.find_element(*JIRA_USERNAME)

    def get_password_field(self):
        return self.driver.find_element(*JIRA_PASSWORD)

    def get_login_button(self):
        return self.driver.find_element(*JIRA_LOGIN_BUTTON)

    def get_worklog_tab(self):
        return self.driver.find_element(*JIRA_WORKLOGTAB)

    def get_log_div(self):
        return self.driver.find_element(*JIRA_LOG_DIV)
