# we have imported the requests module 
import requests 
# defined a URL variable that we will be 
# using to send GET or POST requests to the API
url = "http://localhost:8000/"
token = "abh2x5KKEmmLhhBjxoRlAgin9P9Wzo"
body = """ 
{
  shop {
    name
  }
} 
"""

response = requests.get(url=url, json={"query": body}) 

print("response status code: ", response.status_code) 
# print("response headers: ", response.headers)
# print("response content: ", response.content)
if response.status_code == 200: 
	print("response : ", response.content) 
