from bs4 import BeautifulSoup
import urllib.request as  urlr
import pandas as pd

# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# get the wikipedia page object !
page = urlr.urlopen(wiki)

# print the page
# print(page)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, features="lxml")

# prettify does identation
# print(soup.prettify())

# get the tile
# body = soup.div.string
#
# print(body)

links = soup.find_all('a')
# print(type(link))

# get the each link !
# for link in links:
#     print(link.get('href'))

# find tables
tables = soup.find_all('table')
# print(tables)

# find right table
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
# print(right_table)

#Generate lists
A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th') #To store second column data
    if len(cells) == 6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))


df=pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G

print(df)



