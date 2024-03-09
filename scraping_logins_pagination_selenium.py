import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
from selenium.common.exceptions import NoSuchElementException

# IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
# sudo apt-get install chromium-chromedriver
page_to_scrape = webdriver.Chrome()
page_to_scrape.get("http://quotes.toscrape.com")

# Click on the "Login" link
WebDriverWait(page_to_scrape, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Login"))).click()

# Locate username and password fields
username = WebDriverWait(page_to_scrape, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = WebDriverWait(page_to_scrape, 10).until(EC.presence_of_element_located((By.ID, "password")))

# Input credentials
username.send_keys("admin")
my_pass = getpass.getpass("Enter your password: ")
password.send_keys(my_pass)

# Click the "Login" button
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

with open("scraped_quotes_pagination_selenium.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["QUOTES", "AUTHORS"])

    while True:
        quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
        authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

        # Use list comprehension to encode the entire row
        rows = [(quote.text.encode('utf-8').decode('utf-8'), author.text.encode('utf-8').decode('utf-8')) for quote, author in zip(quotes, authors)]

        # Write the entire list of rows at once
        writer.writerows(rows)

        try:
            page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
            WebDriverWait(page_to_scrape, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text"))
            )
        except NoSuchElementException:
            break

# Close the browser
page_to_scrape.quit()
