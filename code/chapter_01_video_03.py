from bs4 import BeautifulSoup
import pandas as pd
import requests


link = "https://3083218.youcanlearnit.net/rainieststate.html"

page_read = requests.get(link)

soup = BeautifulSoup(page_read.content)

state_result = soup.select_one("p:last-of-type").string

state_result = state_result.strip()
print(state_result)
state_data = {0: ['State'], 1: [state_result]} 

state_data = pd.DataFrame(state_data)
print(state_data)
table = pd.read_html(link, match = "Capital")

table = table.pop()
print(type(table))
table = pd.concat([state_data, table], ignore_index=True)
table = table.rename(columns={0: "info", 1: "stat"})
print(table.T)
print(table.pivot_table(values='stat', columns='info',aggfunc='max'))
# table = table.pivot(columns = "info", values = "stat")
# print(table)
# table_fill = table.bfill()

# table_fill.drop(range(1, len(table_fill)))
# print(table_fill)