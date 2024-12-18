import requests
from bs4 import BeautifulSoup
import datetime

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Search by id
results = soup.find(id='ResultsContainer')

# Search all (by class)
job_cards = results.find_all("div", class_="card-content")

# We create a model for the database
class Job:
    title: str
    subtitle: str
    location: str
    time: datetime.date

    def __init__(self, title, subtitle, location, time):
        self.title = title
        self.subtitle = subtitle
        self.location = location
        self.time = time

jobs = [] 

for job_card in job_cards:
    title = job_card.find("h2", class_="title").text
    subtitle = job_card.find("h3", class_="subtitle").text
    location = job_card.find("p", class_="location").text
    time = job_card.find("time").text
    card = Job(title, subtitle, location, time)
    jobs.append(card)


