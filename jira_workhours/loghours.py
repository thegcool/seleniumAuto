from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import pandas as pd


class GetWorkHrs:
    def __init__(self, driver, wait, container):
        self.driver = driver
        self.wait = wait
        self.container = container

    def get_work_hrs(self):
        users = self.container.find_elements(By.CSS_SELECTOR, "#issue_actions_container .activity-comment-container")
        print(users)
        authors = ["Gokul Bhandari", "Udaya Khanal", "Rina Shrestha", "Ajita Khatiwada", "Karuna Kafle",
                   "Swechhya Bajracharya", "Pragya Gyawali", "Deepen Upreti", "Aayush Kafle", "Sudarshan Chimariya",
                   "Suchita Shakya", "Shashwot Joshi", "Amrit Joshi"]
        columns = ["Author", "Time Spent", "Date", "Comments"]
        rows = []

        for user in users:
            values = {}
            author_element = user.find_element(By.CSS_SELECTOR, ".author .user-hover")
            author = author_element.get_attribute("data-username")

            if author not in authors:
                continue

            values["Author"] = author
            date_element = user.find_element(By.CSS_SELECTOR, ".date")
            date = date_element.get_attribute("title")
            values["Date"] = date

            details_element = user.find_element(By.CSS_SELECTOR, ".activity-comment-inner .action-details")
            time_spent_element = details_element.find_element(By.XPATH,
                                                              ".//li/dl/dt[text()='Time Spent:']/following-sibling::dd")
            time_spent = time_spent_element.text.strip("h")
            values["Time Spent"] = time_spent

            comments_elements = details_element.find_elements(By.XPATH,
                                                              ".//li/dl/dt[text()='Comment:']/following-sibling::dd")
            comments = "\n".join([c.text for c in comments_elements])
            values["Comments"] = comments

            rows.append(values)

        # Create a Pandas DataFrame from the rows
        df = pd.DataFrame(rows, columns=columns)

        # Save the DataFrame to an Excel file
        df.to_excel("output.xlsx", index=False)

        # Read the Excel file back in and convert it to a TableSaw Table
        wb = openpyxl.load_workbook("output.xlsx")
        sheet = wb.active
        data = sheet.values
        columns = next(data)
        table = pd.DataFrame(data, columns=columns)
        table = Table.from_pandas(table)

        return table
