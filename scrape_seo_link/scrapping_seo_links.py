from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://brandee.edu.vn/dien-dan-seo/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scraped_links.csv', 'w', newline='', encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Links'])

for data_row in soup.find_all('tr'):
    data_link = data_row.find_all('td')
    link = data_link[1].text
    print(link)

    csv_writer.writerow([link])

csv_file.close()
