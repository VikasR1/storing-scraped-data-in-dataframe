import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = ''

response = requests.get(url=url)
print(response)

soup = BeautifulSoup(response.text, 'lxml')

company = soup.find_all('div', class_='company-content-wrapper')
# print(len(company))

name =[]
rating =[]
review =[]
comtype=[]
hq=[]
old =[]
employee=[]

for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('p', class_='rating').text.strip())
    # rating.append(i.find_all('p', class_='rating')[0].text.strip())
    review.append(i.find('a', class_='review-count').text.strip())
    comtype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    hq.append(i.find_all('p', class_='infoEntity')[1].text.strip())
    old.append(i.find_all('p', class_='infoEntity')[2].text.strip())
    employee.append(i.find_all('p', class_='infoEntity')[3].text.strip())

# #creating a dictionary

d = {'name' : name, 'rating':rating, 'review':review, 'type':comtype, 'hq':hq, 'old':old, 'employee':employee}

# #creating a dataframe to store all the details

df =pd.DataFrame(d)

# print(df)
# finding shape 
# print(df.shape)
