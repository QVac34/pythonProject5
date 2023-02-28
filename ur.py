# import urllib.request

# opener = urllib.request.build_opener()
# response = opener.open ("https://httpbin.org/")
# print(response.read())

# import requests
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#
#         print(parse_elem_2)
# response = requests.post("https://httpbin.org/"
#                          "post", data="Test data",
#                          headers={"h1": "Test title"})
# response = requests.get("https://httpbin.org/")
# print(response.content)
# print(f"Datatype – {type(response.text)}")
from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print("BTC price", res.text)




