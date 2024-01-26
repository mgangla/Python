import requests
from bs4 import BeautifulSoup
import re

url= "https://jumia.co.ke"

response =requests.get(url)

print(response) 

#response 200 2xx - Successful: The request was successful 

soup = BeautifulSoup(response.text, "html.parser")

# Product page Scrapper
def get_pagecontent(url):
    '''
    This helper function helps get the content from the site 
    and then gets to the required division so as to get the 
    required jumia products.
    parameter:
      url (str): a string of the cite you want to scrape
     returns:
      soup content(bs4 object):  from the required page
    '''
    # begin code here.
    
    return soup





