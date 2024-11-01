import requests
from bs4 import BeautifulSoup
import xlsxwriter

header = ['code','name']
# 3. save to it a XLSX file:
workbook = xlsxwriter.Workbook('crawl_airport.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_row(0, 0, header)
# crawling logic... 
base_url = "https://airportcode.bmcx.com/"
row_number = 0
for i in range(0, 289):
    url = "".join([base_url,f'{i+1}__airportcode'])
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = []
    tr_data = soup.select_one("#main_content ").find('table').find('table').find_all('tr')
    for j in range(1, len(tr_data)):
        td_data = tr_data[j].select("td")
        row = td_data[1].text.strip(),td_data[3].text.strip()
        print(i*30+j, 0, row)
        worksheet.write_row(i*30+j, 0, row)
workbook.close()