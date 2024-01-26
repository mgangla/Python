import requests

# Get data from Json Place holder
# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

response_json = response.json()
print(response_json)

#Post data to a Json Placeholder
#using the post key word

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.post(url)

response_json = response.json()

print("===== This is the data from Json=====")

print(response_json)

#POST Method
# Define new data to create
new_data = {
    "userID": 900,
    "id": 254,
    "title": "Http Post request",
    "body": "The new data posted."
}

url_post = "https://jsonplaceholder.typicode.com/posts"

post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)

#HTTP UPDATe request
#use the put method


#Define data to update
update_data = {
    "userID": 9,
    "id": 2024,
    "title": "Http Update request",
    "body": "Data Dictionary updated."
}

url_post = "https://jsonplaceholder.typicode.com/posts/1"

put_response = requests.put(url_post, json=update_data)

# Print the response
put_response_json = put_response.json()
print(put_response_json)







