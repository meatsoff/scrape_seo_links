from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get('https://brandee.edu.vn/dien-dan-seo/').text
# soup = BeautifulSoup(source, 'lxml')

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

    print()

