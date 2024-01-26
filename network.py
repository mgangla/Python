import requests
data ={'name':'John Doe',
        'age':20
}

#response=requests.get("https://zinduaschool.com")

response=requests.post("https://jsonplaceholder.typicode.com/post", data = data )

#print(response.status_code)
print(response.content)

