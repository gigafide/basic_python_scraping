import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller  # Add this line

# Automatically download and install chromedriver
chromedriver_autoinstaller.install()

# Set up the Chrome driver
browser_driver = webdriver.Chrome()

page_to_scrape = browser_driver
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)
username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

file = open("scraped_quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])
while True:
    quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
    authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)
        writer.writerow([quote.text, author.text])
    try:
        page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        break
file.close()
