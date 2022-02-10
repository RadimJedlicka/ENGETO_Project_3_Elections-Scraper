from pprint import pprint
import requests
from bs4 import BeautifulSoup


url = "https://www.idnes.cz/"
odpoved = requests.get(url)
soup = BeautifulSoup(odpoved.content)
pprint(soup.find_all('a'))