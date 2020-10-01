from bs4 import BeautifulSoup
import csv
from lxml import html
import requests

print('------------------------------------------')
print("Hello, it is simple job search engine for most recent 'Junior Python Developer' job posts across Poland from indeed website")
print('------------------------------------------')
city = input("Job location city [Polish name]: ")
voivd = input("Job location voivodeship [Polish name]: ")
radius = input("Provide your interest distance from chosen city [km]: ")
print('------------------------------------------')
url= "https://pl.indeed.com/praca?q=python+junior&l={}%2C+{}&radius={}".format(city, voivd, radius)
print(url)
print('------------------------------------------')

f = csv.writer(open('JuniorPythonIndeed.csv', 'w'))
f.writerow(['Job post title', 'Company name', 'Location (city and voivodeship)', 'Short summary'])


source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

for jobs in soup.find_all(class_='result'):

    try:
        title=jobs.a.text.strip()
    except Exception as e:
        title = None
    print("Job title:", title)

    try:
        company=jobs.span.text.strip()
    except Exception as e:
        company=None
    print("Company:", company)

    try:
        location = jobs.find('div',class_='location').text.strip()
    except Exception as e:
        location = None
    print("Location:", location)

    try:
        summary = jobs.find('div', class_='summary').text.strip()
    except Exception as e:
        summary = None
    print("Short description:", summary)
    print('------------------------------------------')

    f.writerow([title, company, location,summary])