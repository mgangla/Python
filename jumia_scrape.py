import requests
from bs4 import BeautifulSoup
import csv
import re

url= "https://www.jumia.co.ke/smart-tvs-2282"

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
#url to scrape smart tvs
    url= "https://www.jumia.co.ke/smart-tvs-2282/"

    response =requests.get(url)

    soup_content = BeautifulSoup(response.content, "html.parser")

    return soup_content




## Retrieve product name
def getproductname(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product name
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_name (list) : list of product names
    '''
    #Extract product name from soup
    
    product_name = []

    for name in soup.find_all ('h3',class_='name') :

      return (product_name)
    
    ## Retrieve Brand Name
#def getproductbrand(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product brand
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_brand (list) : list of product brands
    '''
    # begin code here


    #return product_brand

## Retrieve Price
def getproductprice(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here 

    product_price = []

    for price in soup.find_all ('div',class_='prc') :
    
      return product_price

## Retrieve the Discount
def getproductdiscount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product discount
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_discount (list) : list of product discounts
    '''
    # begin code here

    product_discount = []
    for discount in soup.find_all ('div',class_='bdg_dsct_s') :

    
      return product_discount
## Retrieve the Number of reviews.
def getproductreviewcnt(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_reviews (list) : list of product reviews
    '''
    # begin code here

    product_reviews = []

    for reviews in soup.find_all ('div',class_='rev') :
    
      return product_reviews
## Retrieve the ratings.
def getproductrating(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here

    product_rating = []

    for rating in soup.find_all ('div',class_='stars_s') :

    
     return product_rating
## Retrieve the remaining stock.
# getproductcount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract remaining product stock
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_count (list) : list of product items remaining in stock
    '''
    # begin code here
    
   # return product_count
# Bonus Knowledge.
## Determine the actual customer satisfaction rating.
## this function will be computed using pandas
#def getactualrating(reviews, rating):
    '''
    Helper function uses the review and rating columns obtained from the created dataframe
    and then calculate the final actual rating.
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here

    #return actual_rating

# calling out the functions and creating a
## list of list containing the data
soup = get_pagecontent(url)
name = getproductname(soup)
#brand = getproductbrand(soup)
price = getproductprice(soup)
discount = getproductdiscount(soup)
review = getproductreviewcnt(soup)
rating = getproductrating(soup)

list_of_lists = [name,price,discount,review,rating]

## Save and review the product data
with open('jumia_products.csv', 'w') as csvfile:
    fieldnames = ["name","price", "discount", "review", "rating"]

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fieldnames)

    #loop through product list to update csv file
    for fieldname in fieldnames:
        csvwriter.writerow(fieldnames)

    print("Done! All products have been added to CSV file")

## Using pandas to do data manipulation
#jumia = pd.read_csv('jumia_products.csv')
#jumia.head(10)








