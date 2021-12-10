#INSTALL SELENIUM BEFORE RUNNING THIS CODE
#pip3 install selenium
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

#IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
#sudo apt-get install chromium-chromedriver
browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)
username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")
username.send_keys("admin")
#USING GETPASS WILL PROMPT YOU TO ENTER YOUR PASSWORD INSTEAD OF STORING
#IT IN CODE. YOU'RE ALSO WELCOME TO USE A PYTHON KEYRING TO STORE PASSWORDS.
my_pass = getpass.getpass()
password.send_keys(my_pass)
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

file = open("scraped_quotes.csv", "w")
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
