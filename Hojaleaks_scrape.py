import requests
from bs4 import BeautifulSoup
import re
import csv

url= "https://hojaleaks.com"

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

headings = soup.find_all('h1',class_="blog-article-card-title")

print(headings)

data =[]

for heading in headings :
     print (heading.text)

images =soup.find_all('img')

for image in images :
      print(image['src'])

read_times =soup.find_all('span', class_ ="flex.items-center")

for time in read_times :
      print (time.text)


with open('Hojaleaks.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['headings', 'images', 'read_times'])
    writer.writeheader()
    writer.writerows
    
for heading in headings:
        headings = headings.find_all('h1',class_="blog-article-card-title").text.strip()
        images = images.find_all('img').text.strip()
        read_times = read_times.find_all('span', class_ ="flex.items-center").text.strip()

        data.append[{'headings': headings, 'images': images, 'read_times' :read_times description}]

