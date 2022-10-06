from dataclasses import dataclass
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# hiding my ip 
proxies = {
    'http' : '18.220.51.12:80',
    'https' :'18.220.51.12:80'
}
url1= 'http://httpbin.org/ip'
req_proxy = requests.get(url1, proxies = proxies)
print(req_proxy.json())

# hiding ip code ends 

final = pd.DataFrame()

# total pages in ambitionbox are 333 

for j in range(1, 3):

    url = 'https://www.ambitionbox.com/list-of-companies?page{}'.format(j)

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }

    response = requests.get(url=url, headers=headers)
    print(response)

    soup = BeautifulSoup(response.text, 'lxml')

    company = soup.find_all('div', class_='company-content-wrapper')

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

    d = {'name' : name, 'rating':rating, 'review':review, 'type':comtype, 'hq':hq, 'old':old, 'employee':employee}

    df =pd.DataFrame(d)

final = final.append(df, ignore_index=True)
# final = final.concat(df, ignore_index=True)
print(final.shape)

print(final.to_json('list.json'))
print(final.to_csv('list.csv'))

