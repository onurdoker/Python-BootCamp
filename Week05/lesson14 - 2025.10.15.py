"""
Web Scraping:

Web scraping is process of automatically extracting data from web pages.

What can be done with web scraping:
- Track product prices on e-commerce or news websites
- Find top-rated movie or series from film databases
- Analyze trending topics on social media

✅ Allowed
- Scrape publicly accessible data
- Follow robots.txt rules
- Add delays between requests to avoid overloading the server

❌ Not Allowed
- Hack pages that required login.
- Copy copyrighted content without permission
- Send continuous requests that overload the server (DoS-like behavior)
"""

from pyparsing import string_start

# ! First Example
# import requests

# url = "https://google.com"

# response = requests.get(url)

# print("Status code: ", response.status_code)  # Status code:  200

# print(response.text)

# ! Second Example
# import requests
# from bs4 import BeautifulSoup

# url = "https://google.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# print("Title of the web page:", soup.title.text)

# ! Third Example

html_doc = """
<html>
<head><title>Students List</title></head>
<body>
    <div class="students">
        <h1 id="class-title">Class 10-A</h1>
        <ul>
            <li class="student">John Doe</li>
            <li class="student">Mick Jagger</li>
            <li class="student">Michael Jordan</li>
        </ul>
    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

# * Fetching data based on HTML tag name
# print("Title of the Web Page: ", soup.title.text)  # Title of the Web Page:  Students List

print("Information of the div: ", soup.div.text)
"""
Information of the div:
Class 10-A

John Doe
Mick Jagger
Michael Jordan
"""

# * Fetching data based on ID name
# print("Information by ID: ", soup.find(id="class-title").text)  # Information by ID:  Class 10-A


# * Fetching data based on Class name
# * If we want to retrieve only the first piece of information, we use FIND
# print("Information by Class Name: ", soup.find(class_="student").text)  # Information by Class Name:  John Doe

# * If we want to retrieve all the information, we use FIND_ALL
# students = soup.find_all(class_="student")
# for student in students:
#     print(student.text)
"""
John Doe
Mick Jagger
Michael Jordan
"""

# ! Fifth Example
# html_content = """
# <div class="container">
#     <h1>Python Course</h1>
#     <p id="description">Python Programming Language Training</p>
#     <ul>
#         <li class="topic">Variables</li>
#         <li class="topic">Functions</li>
#         <li class="topic">Loops</li>
#     </ul>
# </div>
# """
#
# from bs4 import BeautifulSoup
#
# html_soup = BeautifulSoup(html_content, "html.parser")
#
# print(html_soup.h1.text)  # Python Course
# print(html_soup.find(id="description").text)  # Python Programming Language Training
# print(html_soup.find(class_="topic").text)  # Variables
#
# print(html_soup.find(attrs={"class": "container"}).text)
"""
Python Course
Python Programming Language Training

Variables
Functions
Loops
"""

# topic_tag = html_soup.find_all("li")
# for i, topic in enumerate(topic_tag, start=1):
#     print(f"{i}. {topic.text}")
"""
1. Variables
2. Functions
3. Loops
"""

# ! Sixth Example
# html_content = """
# <div class="container">
#     <h1>Python Course</h1>
#     <p id="description">Python Programming Language Training</p>
#     <ul>
#         <li class="topic">Variables</li>
#         <li class="topic">Functions</li>
#         <li class="topic">Loops</li>
#     </ul>
# </div>
# """
#
# from bs4 import BeautifulSoup
#
# html_soup = BeautifulSoup(html_content, 'html.parser')
#
# print(html_soup.select_one(".container").text)
"""
Python Course
Python Programming Language Training

Variables
Functions
Loops
"""

# print(html_soup.select_one(".container h1").text)  # Python Course
# print(html_soup.select_one("#description").text)  # Python Programming Language Training
#
# print(html_soup.select(".topic"))  # [<li class="topic">Variables</li>, <li class="topic">Functions</li>, <li class="topic">Loops</li>]
# print(html_soup.select(".topic")[0])  # <li class="topic">Variables</li>
# print(html_soup.select(".topic")[0].text)  # Variables
# print(html_soup.select(".topic")[1].text)  # Functions

# ! Seventh Example
# import requests
# from bs4 import BeautifulSoup
#
#
# def basic_scraping_example():
#     url = "https://books.toscrape.com"
#
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#
#         books = soup.select("h3 a")
#
#         print("Books List:")
#         for i, book in enumerate(books[:10], 1):  # first 10 books listed
#             print(f"{i:2d}. {book.text.strip()}")
#
#     except Exception as error:
#         print("Error: ", error)
#
#
# basic_scraping_example()

# ! Eighth Example
