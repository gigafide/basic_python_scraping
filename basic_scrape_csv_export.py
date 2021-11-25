#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

#IMPORT CSV LIBRARY
import csv

#OPEN A NEW CSV FILE. IT CAN BE CALLED ANYTHING
file = open('scraped_quotes.csv', 'w')
#CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

#CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Quote', 'Author'])

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("http://quotes.toscrape.com")
#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE
quotes = soup.findAll('span', attrs={'class':'text'})

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
authors = soup.findAll('small', attrs={"class":"author"})

#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
    #WRITE EACH ITEM AS A NEW ROW IN THE CSV
    writer.writerow([quote.text, author.text])
#CLOSE THE CSV FILE
file.close()
