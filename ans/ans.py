from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.ttfi.org/events/ranking/MjAyNA==/NDk="

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')




data = []
# venue = ["Jimmy George Indoor Stadium, Vellayambalam Trivandrum", "Sama Indoor Sports Complex, Vspf, Vadodara (gujarat)", "Vijayawada (andhra Pradesh)", "Multipurpose Hall, Tau Devi Lal Stadium, Sector 3, Panchkula (haryana)", "Abhay Prashal Stadium, Indore (madhya Pradesh)", "Kangra, Himachal Pradesh"]

rows = soup.find_all('tr')[3:]
# print(rows)

for row in rows:
    cols = row.find_all('td')
    data.append({
        'TTFI ID': int(cols[1].text.strip()),
        'name': cols[2].text.strip(),
        'state': cols[3].text.strip(),
        'DOB': cols[4].text.strip(),
        'ranking': int(cols[12].text.strip())
    })
    
print(data)



df = pd.DataFrame(data)
# print(df)

one = df[(df['ranking'] > 18) & (df['ranking'] < 26)]
print(one)

# print(df['DOB'])
# two = df[df['DOB'][-1:-4]]




from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['eval']
collection = db['tt']

collection.insert_many(data)

ans = collection.find({'ranking': 11})

for i in ans:
    print(i)




ans = collection.find({'state': 'TN'})

for i in ans:
    print(i)
