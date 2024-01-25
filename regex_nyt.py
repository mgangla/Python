import requests
from bs4 import BeautifulSoup
import re

#task Use regular expression patterns to get #
#phone  numbers, emails, and hyperlinks from the newyork times website

url= "https://nytimes.com"


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#hyperlinks 

   #Find all the String that matches with the pattern
regex = r"(https?://\S+)"

hyperlinks  = re.findall(regex,response.text)

for hyperlink in hyperlinks:
    print(hyperlink)


#extract phone number
print("===== These are the phone numbers on nytimes.com=====")

#Find all the String that matches with the phone number
regex1 = r"(^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$)"
phone_number  = re.findall(regex1,response.text)

print(phone_number)


#extract email addresses
print("===== These are the email addresses on nytimes.com=====")

#Find all the String that matches with the phone number
regex_email= r"^[a-zA-Z0-9_. +-]+@[a-zA-Z0-9-]+\. [a-zA-Z0-9-.]+$"

# r"^[\w\d_+.-]+@[\w\d]+.[\w.d]+$"
email  = re.findall(regex_email,response.text)

print(email)
