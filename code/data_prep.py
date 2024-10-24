# exercise 1
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin 
import requests
import re
import numpy as np

dollar_values = {'dollar_values': ['$10.00', '$1,00', '$10', '$10.01', '$1,000.01']} 
# VERSION 1
# 
# numbers = []
# for i in dollar_values.values():
#   for j in i:
#     print(j)
#     number = re.search(r'[0-9.,]+',j).group(0)
#     if len(re.findall(r'[.]', number)) != 0:
#       print(re.search(r'.', number).group(0))
#       number = number.replace(',', '')
#       numbers.append(float(number))
#     else:
#       print(re.search(r'[.]', number))
#       number = re.sub(r'(,\d+$)','', number)
#       print(number)
#       numbers.append(float(number))

# print(numbers) 

def check_decimal(x):
  if len(re.findall(r'[.]', x)) != 0:
    x = x.replace(',','')
    return x
  else:
    x = re.sub(r',(\d{2})','', x)
    return x

dollar_data = pd.DataFrame(dollar_values)
dollar_data['dollar_values'] = dollar_data['dollar_values'].apply(lambda x : re.sub('\$', '', x))
dollar_data['dollar_values'] = dollar_data['dollar_values'].apply(lambda x : check_decimal(x))
dollar_data['dollar_values'] = dollar_data['dollar_values'].astype(float)


# exercise 2 
painful_strings = {'painful_strings':
                   ['usePython', 'pandasForLife', 'Python is helpful']}
strings = pd.DataFrame(data = painful_strings)

def split_string(x):
  xx = re.split(r'(?=[A-Z])', x)
  new = ' '.join(xx)
  return new


strings['new_strings'] = strings['painful_strings'].apply(lambda x: split_string(x))