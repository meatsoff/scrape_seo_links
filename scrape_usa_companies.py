from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
web_info = requests.get(url)
soup = BeautifulSoup(web_info.text, 'lxml')

dt_table = soup.find_all('table')[1]
tb_titles = dt_table.find_all('th')
tb_col_name = [title.text.strip() for title in tb_titles]

df = pd.DataFrame(columns=tb_col_name)
col_data = dt_table.find_all('tr')
for row in col_data[1:]:
    row_data = row.find_all('td')
    row_individual_data = [dt.text.strip() for dt in row_data]
    length = len(df)
    df.loc[length] = row_individual_data
print(df)

