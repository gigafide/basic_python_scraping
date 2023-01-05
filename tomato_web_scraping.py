from bs4 import BeautifulSoup 
import requests

#request page and store as a var
page_to_scrape = requests.get("https://www.gardenersworld.com/plants/top-tomato-varieties-to-grow/")
#use BS to parse the HTML and store as a var
soup = BeautifulSoup(page_to_scrape.text,'html.parser')

#find all the items in the page with the class attrs of "inline"
#store it as a variable
names = soup.find_all('h3',attrs={'class':'mb-sm heading-3'})

#find all the items in the page with the strong tags with no attrs
#types = soup.find('p', attrs={'class':''})
#find the next item after "types"


types = soup.find_all('strong',{'class':''},string = 'Type:')




  
# print("20 of the best tomatoes to grow:")
#loop
#for name, type in zip(names, types):
  #print(type.text.strip("Tomato "+ "'" + "'") + "-" + type.text)

for type in types:
 print(type.text)
