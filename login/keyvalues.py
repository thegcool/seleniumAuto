import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

JIRA_USERNAME = (By.ID, "login-form-username")
JIRA_PASSWORD = (By.ID,"login-form-password")
JIRA_LOGIN_BUTTON =(By.CLASS_NAME,"aui-button-primary")
JIRA_WORKLOGTAB =(By.ID,"worklog-tabpanel")
JIRA_LOG_DIV =(By.ID,"issue_actions_container")
JIRA_GET_USERS =(By.XPATH,"//div[contains(@id, 'worklog-')]")
JIRA_AUTHORS =(By.XPATH,"a[contains(@id, 'worklogauthor_')]")

#JIRA_LOGIN_BUTTON =(By.CLASS_NAME,"aui-button-primary")

