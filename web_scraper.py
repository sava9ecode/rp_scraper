import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2",
    string=lambda text: "python" in text.lower(),
)

count = 0
for job in python_jobs:
    count += 1
    great_grandfather = job.parent.parent.parent
    title_element = great_grandfather.find("h2", class_="title")
    title_company = great_grandfather.find("h3", class_="company")
    title_location = great_grandfather.find("p", class_="location")

    link_url = great_grandfather.find_all("a")[1]["href"]

    print(
        f"""
Company #{count}:
{title_element.text.strip()}
{title_company.text.strip()}
{title_location.text.strip()}
Apply here: {link_url}"""
    )
