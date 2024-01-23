import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
}

source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers).text
soup = BeautifulSoup(source, 'html.parser')

# Movie Titles
with open('titles.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title'])

    titles = soup.find_all('h3', class_='ipc-title__text')

    for title in titles[1:]:
        title_text = title.text.strip()
        csv_writer.writerow([title_text])

# Movie Years
with open('years.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Year'])

    metadata_divs = soup.find_all('div', class_='sc-1e00898e-7 hcJWUf cli-title-metadata')

    for metadata_div in metadata_divs:
        year = metadata_div.find('span', class_='sc-1e00898e-8 hsHAHC cli-title-metadata-item').get_text(strip=True)
        csv_writer.writerow([year])
        
        # Movie Ratings
with open('ratings.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Rating'])

    rating_spans = soup.find_all('span', class_='ipc-rating-star--imdb')

    for rating_span in rating_spans:
        rating = rating_span.text.strip()
        csv_writer.writerow([rating])