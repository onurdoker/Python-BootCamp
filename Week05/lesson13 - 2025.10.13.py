"""
API (Application Programming Interface)

An APIis a tool allows different software systems to communicate with each other.

Simple Analogy:
You can think of an API as a waiter in a restaurant.
You (the client) place an order (a request) for the dish (data) you want from the kitchen (the server) through the waiter (the API).
The waiter delivers your order to the kitchen and then bring back the meal (the response) to you.

Real-life example:
Restaurant menu -> Place order (request) -> Kitchen prepares -> Food is served (response)

Why is it used?

Data Exchange:
Allow one program to securely and reliably access data from another application. 
(Example: accessing Twitter data, weather information or exchange rates)

Functionality Share:
Enables your application to use the features of another services.
(Example: Integrating payment systems or map services)

REST API: A REST API is an API structure that works over the HTTP protocol and return data in JSON or XML format.

HTTP methods: GET (Retrieve data), POST (Send (create) data), PUT (Update existing data), DELETE (Delete data).
"""

import requests

# ! First Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts/2')
#
# print(response)  # 200 => successfully
# print("Response Code: ", response.status_code)  # 200

"""
Status codes:
200: OK
201: Created
202: Accepted
404: Not Found
403: Forbidden
405: Method Not Allowed
406: Not Acceptable
408: Request Timeout
409: Conflict
410: Gone
500: Internal Server Error
"""

# ! Second Example
# response = requests.get('https://jsonplaceholder.typicode.com/pos')
#
# print(response)  # 404 => unsuccessfully
# print("Response Code: ", response.status_code)  # 404

# ! Third Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
#
# print(response.text)
# print(type(response.text))  # str

# ! Fourth Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
#
# data_json = response.json()
# print(type(data_json))  # <class 'list'>
# print(len(data_json))  # 100

# ! Fifth Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data_json = response.json()
# for data in data_json:
#     print(f'{data}')

# ! Sixth Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data_json = response.json()
# for data in data_json[:2]:
#     print(f'{data}')

# ! Seventh Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data_json = response.json()
# for data in data_json[:2]:
#     for titles in data:
#         print(f"{titles}:\t{data[titles]}")

# ! Eighth Example
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
#
# print("Response Code: ", response.status_code)  # <Response [200]>
# print(response.status_code)  # 200
# print(response.json())
# print(type(response.json()))  # <class 'dict'>
# print(len(response.json()))  # 4

# !Nineth Example
# url = 'https://api.github.com'
# response = requests.get(url)
#
# print("Response Code: ",
#       response.status_code)
#
# if response.status_code == 200:
#     print("Request Successful")
# else:
#     print("Request Failed, Error Code: ",
#           response.status_code)

# ! Tenth Example
# url = 'https://api.github.com'
# response = requests.get(url)
#
# data = response.json()
# print(data)
# print(type(data))  # <class 'dict'>

# ! Eleventh Example
# url = 'https://api.github.com'
# response = requests.get(url)
#
# data = response.json()
# for key, value in data.items():
#     print(key,
#           value)

# ! Twelve Example
# url = 'https://jsonplaceholder.typicode.com/users/1'
# response = requests.get(url)
#
# print("Response Code: ",
#       response.status_code)  # Response Code:  200
#
# if response.status_code == 200:
#     user_data = response.json()
#     print(f"User Name: {user_data['name']}")
#     print(f"E-mail: {user_data["email"]}")
#
#     print(f"City: {user_data["address"]["city"]}")
# else:
#     print("Request Failed, Error Code: ",
#           response.status_code)

# ! Thirteenth Example

# * First Practice (Successfully connection)
# try:
#     url = 'https://jsonplaceholder.typicode.com/users/1'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         user_data = response.json()
#         print(f"User Name: {user_data['name']}")
#         print(f"E-mail: {user_data["email"]}")
#
#         print(f"City: {user_data["address"]["city"]}")
#     else:
#         print("Request Failed, Error Code: ",
#               response.status_code)
# except requests.exceptions.RequestException as error:
#     print(f"Request Failed, Error Code: {error}")

# * Second Practice (timeout error)
# try:
#     url = 'https://jsonplaceholder.typicode.com/users/1'
#     response = requests.get(url,
#                             timeout=0.05)
#
#     if response.status_code == 200:
#         user_data = response.json()
#         print(f"User Name: {user_data['name']}")
#         print(f"E-mail: {user_data["email"]}")
#
#         print(f"City: {user_data["address"]["city"]}")
#     else:
#         print("Request Failed, Error Code: ",
#               response.status_code)
# except requests.exceptions.RequestException as error:
#     print(f"Request Failed, Error Code: {error}")


# ! Fourteenth Example
# import json
#
# url = 'https://jsonplaceholder.typicode.com/invalid-url'
#
# try:
#     response = requests.get(url,
#                             timeout=5)
#     response.raise_for_status()
#
#     data = response.json()
#     print("Data fetch successfully")
#
# except requests.exceptions.HTTPError as error_http:
#     print(f"HTTP Error: {error_http}")  # 404 Not Found
# except requests.exceptions.ConnectionError as error_connection:
#     print(f"Connection Error: {error_connection}")  # Connection Errors
# except requests.exceptions.Timeout as error_timeout:
#     print(f"Timeout Error: {error_timeout}")  # Timeout Errors
# except requests.exceptions.RequestException as error_request:
#     print(f"Request Error: {error_request}")
# except json.JSONDecodeError as json_error:
#     print(f"JSON Decode Error: {json_error}")


# ! Fifteenth Example
# import datetime
#
# try:
#     url = 'https://jsonplaceholder.typicode.com/users/1'
#
#     start = datetime.datetime.now()
#     response = requests.get(url)
#     finish = datetime.datetime.now()
#     print(f"Time to fetch data from the API: {(finish - start).total_seconds():.3f} seconds\n")
#
#     if response.status_code == 200:
#         user_data = response.json()
#         print(f"User Name: {user_data['name']}")
#         print(f"E-mail: {user_data["email"]}")
#
#         print(f"City: {user_data["address"]["city"]}")
#     else:
#         print("Request Failed, Error Code: ",
#               response.status_code)
# except requests.exceptions.RequestException as error:
#     print(f"Request Failed, Error Code: {error}")

# ! Sixteenth Example
# def crypto_price(crypto_name):
#     url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name.lower()}&vs_currencies=usd,try"
#
#     try:
#         response = requests.get(url,
#                                 timeout=5)
#         if response.status_code == 200:
#             data = response.json()
#
#             if crypto_name.lower() in data:
#                 usd = data[crypto_name.lower()]["usd"]
#                 try_price = data[crypto_name.lower()]["try"]
#                 print(f"✅ {crypto_name.capitalize()}: ${usd:,.2f} | ₺{try_price:,.0f} ")
#             else:
#                 print(f"❌ {crypto_name} not found, please try again later")
#
#         else:
#             print(f"⚠️ API request failed, status code: {response.status_code}")
#
#     except requests.exceptions.ConnectionError:
#         print(f"❌ Internet connection error or cannot reach API")
#     except requests.exceptions.Timeout:
#         print("⏱️ API request timed out")
#     except Exception as error:
#         print(f"🚨 Unexpected error: {error}")
#
# print("🪙 Wellcome to the Cryptocurrency Price Tracker!")
# print("Supported Examples: bitcoin, ethereum, cardano, solana, dogecoin\n")
#
# while True:
#     coin = input("Enter the name of the cryptocurrency you would like to use (press 'q' to quit): ")
#     if coin.lower() == "q":
#         print("Exiting...")
#         break
#     if not coin:
#         print("Please enter a cryptocurrency you would like to use.")
#         continue
#
#     crypto_price(coin)
