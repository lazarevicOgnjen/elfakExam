import os
import requests
from bs4 import BeautifulSoup
import yearRI

url = os.getenv('url')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('tr')
header = soup.find('tr')
columns = len(header.find_all('td'))

clean_header = header.get_text(separator=' | ', strip=True)
h = f"| {clean_header} |\n"


with open ("schedule.md", "w", encoding="utf-8") as f:
		f.write(f'**url: [{url}]({url})**')



tableName = ['I godina', 'II godina', 'III godina', 'IV godina']
i = 0
with open ("schedule.md", "a", encoding="utf-8") as f:
	while i < 4:
		f.write(f'\n\n\n**{tableName[i]}**\n\n')
		f.write(h)
		f.write('|')
		c = 0
		while c < columns:
			f.write(':-:|')
			c += 1
		f.write('\n')

		for subject in yearRI.year(i+1):
			for row in rows:
				clean_row = row.get_text(separator=' | ', strip=True)
				if subject in clean_row:
					s = f"| {clean_row} |\n"
					f.write(s)
					break
		
		i += 1
		




