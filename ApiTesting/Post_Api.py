import json
import requests
from pprint import pprint

url = "https://node-fake-api-server.herokuapp.com/user"
payload = {"external_id": "postman"}
headers = {'Content-Type': "application/json,text/plain",
           'X-FakeAPI-Action': 'register'
           }
response = requests.request("POST", url, data=payload, headers=headers)
print("Response iterLines :")
pprint(response.iter_lines())
print("Response Raw :")
pprint(response.raw)
print("Response Request :")
pprint(response.request)
print("Response Content :")
pprint(response.content)
print("Response Cookies :")
pprint(response.cookies)
print("Response Status Code :")
pprint(response.status_code)
print("Response Headers :")
pprint(response.headers)
print("Response Encoding :")
pprint(response.encoding)
print("Response JSon :")
pprint(response.json())
print("Response Url :")
pprint(response.url)
print("Response Reason :")
pprint(response.reason)
print("Response History :")
pprint(response.history)
print("Response Elapsed :")
pprint(response.elapsed)
print("Response raise for status :")
pprint(response.raise_for_status())
print("Response isRedirect :")
pprint(response.is_redirect)
print("Response isPermanent Redirect :")
pprint(response.is_permanent_redirect)
print("Response OK :")
pprint(response.ok)
print("Response Links :")
pprint(response.links)
print("Response iterContent :")
pprint(response.iter_content())
data = response.json()
username = data['username']
password = data['password']
token = data['auth_token']
print("Response Data Extraction :")
print("userName:%s\nPassword:%s\nAuthorization Token:%s"
      % (username, password, token))

# url1 = "https://node-fake-api-server.herokuapp.com/"
# payload1 = {
#     "method": "get",
#     "path": "/hello-world",
#     "responses": [
#         {
#             "status": 200,
#             "content": "Hello world!",
#             "content_type": "text/plain"
#         }
#     ]
# }
# headers1 = {'Content-Type': "application/json,text/plain",
#             'X-FakeAPI-Action': 'record'
#             }
# resp = requests.request("PUT", url1, data=payload1, auth=(username, password), headers=headers1)
#
# pprint(resp.status_code)
# pprint(resp.headers)
# pprint(resp.encoding)
# pprint(resp.json())
# pprint(resp.url)
#
# url2 = f"https://node-fake-api-server.herokuapp.com/hello-world?who=bar"
# headers2 = {'X-FakeAPI-Action': 'record'}
#
# response2 = requests.request("GET", url2, auth=(username, password), headers=headers2)
# print(response2.url)
# print(response2.request)
# print(response2.content)
# print(response2.cookies)
# print(response2.status_code)
# print(response2.headers)
# print(response2.encoding)
# print(response2.json())
# print(response2.reason)
# print(response2.history)
# print(response2.elapsed)
# print(response2.is_redirect)
# print(response2.is_permanent_redirect)
# print(response2.ok)
# print(response2.links)
# print(response2.iter_content())
