import requests
from bs4 import BeautifulSoup
from utils.db import get_snowflake_engine
from utils.models import Base, StgJobs
from sqlalchemy.orm import Session
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Search by id
results = soup.find(id='ResultsContainer')

# Search all (by class)
job_cards = results.find_all("div", class_="card-content")

jobs = [] 

engine = get_snowflake_engine()

# Create table esqueletons
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     for job_card in job_cards:
#         title = job_card.find("h2", class_="title").text.strip()
#         subtitle = job_card.find("h3", class_="subtitle").text.strip()
#         location = job_card.find("p", class_="location").text.strip()
#         time = job_card.find("time").text.strip()
#         job = StgJobs(
#             title=title,
#             subtitle=subtitle,
#             location=location,
#             date=time)
#         jobs.append(job)
#         # print(job)

#     session.add(job)
#     session.commit()

    # try:
    #     results = connection.execute(parsed_query("SELECT CURRENT_VERSION()")).fetchone()
    #     print(results[0])
    # finally:
    #     connection.close()
    #     engine.dispose()

