# exercise 1
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin 
import requests
link = "https://3083218.youcanlearnit.net/geographytables.html"

data = pd.read_html(link)
print(data)
print(type(data))
print(type(type(data)))
print(data[2].sort_values(by= 'Total Area in Sq Mi', ascending=False).iloc[0])

area = data.pop()
print(type(area))
print(list(area.sort_values(by= 'Total Area in Sq Mi', ascending=False).values).pop())

# exercise 2
base_link = 'https://hplussport.net/#people'
# data = pd.read_html('https://hplussport.net/#people',attrs={'name':'card-name'})
# print('data')
session = requests.Session()

html = session.get(base_link).content
soup = bs(html, "html.parser")
print(soup)
names = []
titles = []
for el in soup.find_all('h3'):
  names.append(el.string)
for el in soup.find_all('h4'):
  titles.append(el.string)
names_titles = pd.DataFrame(data = {'names':names,  'titles':titles})
print(names_titles)
# alternative way with select
print(soup.select(".card-name")[0].text )

# exercise 3
link = "https://3083218.youcanlearnit.net/rainieststate.html"
html = requests.get(link).content
soup = bs(html,features="html.parser")

len_tr = len(soup.find_all('td'))
data = soup.find_all('td')
vals = []
cols = []
print(data)
for i in range(len_tr):
  if i%2 == 0:
    cols.append(data[i].string)
  else:
    vals.append(data[i].string)
df = pd.DataFrame(data = {'attribute': cols, 'values': vals})
print(df.T)

# exercise 4
linkx = 'https://3083218.youcanlearnit.net/dataTable.html'
linkx = 'https://3083218.youcanlearnit.net/rank.json?_=1728829263114'
linkx = 'https://3083218.youcanlearnit.net/rank.json?_=1662342121475'
page = requests.get(url=linkx)
print(page)

# exercise 5
df=[]
base_link = 'https://pixelford.com/api/image/id/'
for i in range(20):
  link = base_link + str(i)
  _json = requests.get(link)
  data = pd.read_json(_json.content)
  df.append(data) 