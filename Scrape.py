import urllib2, csv
# Imports urllib2 and csv to visit websites with Python. 

from bs4 import BeautifulSoup
# Imports the tool BeautifulSoup from bs4 package

outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)
# Opens a file named jaildata.csv and calls a csv writer

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()
# Downloads the Boone Cuunty webpage and grabs content from html

soup = BeautifulSoup(html, "html.parser")
# Parse the html using BeautifulSoup and store in variable 'soup'

tbody = soup.find('tbody', {'class': 'stripe'})
# Finds a stripe class of the tbody tag in the html

rows = tbody.find_all('tr')
# Finds tr tag in rows from the html

for row in rows:
# Begins a loop

    cells = row.find_all('td')
    # Creates cells and get value from td tag in rows

    data = []
    # Creates an empy list called data
    
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
        # Adds texts in cells encoded in utf-8 to the data list that has been just created

    writer.writerow(data)
    # Writes the row of data