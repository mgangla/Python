#requests
#requests;


#BeautifulSoup
#pip install requests beautifulsoup4 ;
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.zinduaschool.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print (soup)

#extract data

paragraphs =soup.find_all ('p')

print (paragraphs)

for paragraph in paragraphs :
    print(paragraph.text)

#store data in a csv
with open("data.csv","w",newline= '')as csvfile :
    writer=csv.writer(csvfile)
    writer.writerow([paragraphs])

    for paragraph in paragraphs :
        writer.writerow([paragraph.text])
