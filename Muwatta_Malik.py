# Import the necessary libraries
import pandas as pd
import requests
import bs4 as soup
import csv

# Specify the URL
all_links = []
for i in range(1 , 62):
    links_url = 'https://sunnah.com/malik/' + str(i)
    all_links.append(links_url)
print("--------------------", all_links)


# Initialize your lists
chapter_title_name = []
english_hadith = []
hadith_references = []

# Loop through your links
for i in all_links:
    url = i
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    response.status_code
    page_soup = soup.BeautifulSoup(response.text, 'html.parser')

    # Extract chapter title
    chapter_title = page_soup.find('div', class_='book_page_english_name')
    chapter_title_name.append(chapter_title.text.strip())

    # Extract English hadith
    english_hadith_full = page_soup.find_all("div", {"class": "english_hadith_full"})
    for i in english_hadith_full:
        english_hadith.append(i.text)

    # Extract hadith references
    hadith_reference = page_soup.find_all('table', class_='hadith_reference')
    for c in hadith_reference:
        hadith_references.append(c.text)

# Ensure that chapter_title_name has the same length as english_hadith and hadith_references
chapter_title_name = chapter_title_name[:len(english_hadith)]
print("--------------------", chapter_title_name)
# Combine the data into a list of tuples
data = zip(chapter_title_name, english_hadith, hadith_references)
print("--------------------", data)
# Specify the CSV file path
csv_file_path = "Muwatta_Malik.csv"

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(['Chapter Title', 'English Hadith', 'Hadith References'])
    
    # Write the data rows
    csv_writer.writerows(data)

print("Data has been saved to", csv_file_path)
