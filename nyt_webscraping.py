import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup)
articles = soup.find_all('article', class_='css-8atqhb')
data = []



with open('nytimes.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)

    for article in articles[:10]:
        title = article.find_all('h2', class_='css-1vvhd4r').text.strip()
        description = article.find_all('p', class_='css-1echdzn').text.strip()
        data.append({'title': title, 'description': description})