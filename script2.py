import requests
from bs4 import BeautifulSoup

url='https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

blog_titles = soup.findAll('div')
for title in blog_titles:
    print(title.text)