"""
Web Automation:

Understanding what web automation is and why it is used
Installing and using Selenium WebDriver
Finding and interacting with elements on web pages
Filling out forms, clicking buttons, and navigating pages
Developing automation projects with real-life examples


Use Cases:

- Test Automation (QA)
- Data Collection (alternative of Web Scraping)
- Automatically Form Filled
- Bot development (e.g., price tracking)


What is Selenium?
It is an open-source web automation tool
It programmatically controls browsers (Chrome, Firefox, Edge, etc.)
Selenium WebDriver: Communicates directly with the browser


Reasons to Use Selenium:
- To fetch pages loaded with JavaScript
- For actions like filling out forms or clicking buttons
- For automate browser-based tests


BeautifulSoup vs Selenium
BeautifulSoup
- Only an HTML parser
- Ideal for static pages
- Fast and lightweight

Selenium
- Controls a real browser
- Can execute JavaScript
- Ideal for dynamic pages
- Slower but more powerful


"""

# ! First Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
# brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
# chromedriver_path = (
#     "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
# )
#
# options = Options()
# options.binary_location = brave_path
#
# service = Service(chromedriver_path)
#
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://www.google.com")
#
# time.sleep(3)
# driver.quit()


# ! Second Example
"""
Methods to Find Web Elements
Selenium provides 8 main methods to locate HTML elements

- find_element(By.ID, "id")
- find_element(By.NAME, "name")
- find_element(By.CLASS_NAME, "class")
- find_element(By.TAG_NAME, "div")
- find_element(By.XPATH, "//input[@name='q']")
- find_element(By.CSS_SELECTOR, "input[name='q']")
- find_element(By.LINK_TEXT, "Gmail")
- find_element(By.PARTIAL_LINK_TEXT, "Gma")
"""

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
# brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
# chromedriver_path = (
#     "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
# )
#
# options = Options()
# options.binary_location = brave_path
#
# service = Service(chromedriver_path)
#
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://www.google.com")
#
# driver.implicitly_wait(5)  # Upload page
#
# search_box = driver.find_element(By.NAME, "q")
# time.sleep(2)
#
# search_box.send_keys("python")
# search_box.submit()
#
# time.sleep(5)
# driver.implicitly_wait(5)
# driver.quit()

# ! Third Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = (
#         "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#     )
#
#     chrome_options = Options()
#     chrome_options.binary_location = brave_path
#     chrome_options.add_argument("--start-maximized")  # to full page
#     chrome_options.add_argument("--disable-extensions")  # to disable extensions
#     chrome_options.add_argument("--disable-notification")  # to disable notifications
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     driver.implicitly_wait(5)
#
#     return driver
#
#
# def selenium_test():
#     driver = setup_driver()
#
#     driver.get("https://www.google.com")
#
#     driver.implicitly_wait(2)  # Upload page
#
#     search_box = driver.find_element(By.NAME, "q")
#     time.sleep(2)
#
#     search_box.send_keys("python")
#     search_box.submit()
#     time.sleep(3)
#
#     driver.implicitly_wait(2)
#
#     print(driver.title)
#     driver.implicitly_wait(2)
#
#     time.sleep(3)
#     driver.quit()
#
#
# selenium_test()

# ! Fourth Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = (
#         "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#     )
#
#     chrome_options = Options()
#     chrome_options.binary_location = brave_path
#     # chrome_options.add_argument("--start-maximized")  # to full page
#     chrome_options.add_argument("--disable-extensions")  # to disable extensions
#     chrome_options.add_argument("--disable-notification")  # to disable notifications
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     driver.implicitly_wait(5)
#
#     return driver
#
#
# def selenium_test():
#     driver = setup_driver()
#
#     driver.get("https://www.google.com")
#
#     driver.implicitly_wait(2)  # Upload page
#
#     search_box = driver.find_element(By.NAME, "q")
#     time.sleep(2)
#
#     search_box.send_keys("python")
#     search_box.submit()
#     time.sleep(3)
#
#     driver.save_screenshot("test.png")
#
#     driver.implicitly_wait(2)
#
#     time.sleep(3)
#     driver.quit()
#
#
# selenium_test()

# ! Fifth Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = (
#         "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#     )
#
#     chrome_options = Options()
#     chrome_options.binary_location = brave_path
#     # chrome_options.add_argument("--start-maximized")  # to full page
#     chrome_options.add_argument("--disable-extensions")  # to disable extensions
#     chrome_options.add_argument("--disable-notification")  # to disable notifications
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     driver.implicitly_wait(5)
#
#     return driver
#
#
# def selenium_test():
#     driver = setup_driver()
#
#     try:
#         driver.get("https://www.google.com")
#
#         driver.implicitly_wait(2)  # Upload page
#
#         search_box = driver.find_element(By.NAME, "qk")
#         time.sleep(2)
#
#         search_box.send_keys("python")
#         search_box.submit()
#         time.sleep(3)
#
#         driver.implicitly_wait(2)
#
#         time.sleep(3)
#         driver.quit()
#
#     except Exception as error:
#         print(f'An error occurred: {error}')
#     finally:
#       print('Browser closed.')
#
#
# selenium_test()

# ! Sixth Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.binary_location = brave_path
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service,
#                               options=chrome_options)
#
#     driver.implicitly_wait(5)
#
#     return driver
#
# def selenium_test_1():
#     driver = setup_driver()
#
#     try:
#         driver.get("https://www.google.com")
#
#         search_box = driver.find_element(By.NAME,
#                                          "q")
#         driver.implicitly_wait(2)  # Upload page
#         time.sleep(3)
#
#         search_box.send_keys("python")
#         search_box.submit()
#         time.sleep(3)
#
#         driver.implicitly_wait(2)
#
#         print(driver.title)
#         driver.implicitly_wait(2)
#
#         time.sleep(3)
#         driver.quit()
#     except Exception as error:
#         print(f'An error occurred: {error}')
#    finally:
#       print('Browser closed.')
#

#! Seventh Example
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = (
#         "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#     )
#
#     chrome_options = Options()
#     # chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.binary_location = brave_path
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     # driver.implicitly_wait(5)
#
#     return driver
#
#
# def selenium_test():
#     driver = setup_driver()
#
#     try:
#         driver.get("https://www.hepsiburada.com")
#
#         try:
#             print("Cookies are accepted")
#
#             accept_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable(By.ID, "onetrust-accept-btn-handler")
#             )
#
#             # accept_button = driver.find_element(
#             #     By.XPATH, '// *[ @ id = "onetrust-accept-btn-handler"]'
#             # )
#
#             accept_button.click()
#             print("Cookies are accepted")
#
#         except:
#             print("There was an error occurred Cookies are not accepted")
#         driver.implicitly_wait(5)
#
#         # * Using ID
#         # element = driver.find_element(By.ID, "seo-root")
#         # print(element.text)
#
#         # * Using Class_name
#         # element = driver.find_element(By.CLASS_NAME, "b4LLXnK8oFgCSaa4Ni13")
#         # print(element.text)
#
#         # * Using link
#         element = driver.find_element(By.LINK_TEXT, "Hakkımızda")
#         # element = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.LINK_TEXT, "Hakkımızda"))
#         # )
#
#         print(element.get_attribute("href"))
#         element.click()
#
#         time.sleep(15)
#         driver.implicitly_wait(5)
#
#     except Exception as error:
#         print(f"An error occurred: {error}")
#     finally:
#         print("Browser closed")
#         # driver.quit()
#
#
# selenium_test()


# ! Sixth Example
# * https://demoqa.com/automation-practice-form
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# def setup_driver():
#     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
#
#     chromedriver_path = (
#         "/Users/odoker/Documents/Projects/Python/Python-BootCamp/chromedriver"
#     )
#
#     chrome_options = Options()
#     # chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.binary_location = brave_path
#
#     service = Service(chromedriver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     # driver.implicitly_wait(5)
#
#     return driver
#
#
# def filling_form():
#     driver = setup_driver()
#
#     try:
#
#         driver.get("https://demoqa.com/automation-practice-form")
#
#         first_name = driver.find_element(By.ID, "firstName")
#         first_name.send_keys("Onur")
#
#         last_name = driver.find_element(By.ID, "lastName")
#         last_name.send_keys("DOKER")
#
#         email = driver.find_element(By.ID, "userEmail")
#         email.send_keys("odoker@msn.com")
#
#         # * Using css selector via filling radio buttons
#         # gender = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]')
#         # gender.click()
#
#         # * Using JS Script to filling radio buttons
#         driver.execute_script("document.getElementById('gender-radio-1').click()")
#
#         mobile = driver.find_element(By.ID, "userNumber")
#         mobile.send_keys("1234567")
#
#         driver.implicitly_wait(5)
#         time.sleep(5)
#
#     except Exception as error:
#         print(f"An error occurred: {error}")
#     finally:
#         print("Browser closed")
#         driver.quit()
#
#
# filling_form()
