from bs4 import BeautifulSoup
from cl_listing import cl_listing
import requests
import uuid

if __name__ == '__main__':

    page = 0
    listings = {}

    for x in range(0, 1):

        URL = "https://cnj.craigslist.org/d/electronics/search/ela?s=" + str(page) + "&postal=07920&search_distance=10"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find("ul",  attrs = {'class':'rows'})
        for row in table.findAll("li",  attrs = {'class':'result-row'}):

            id = str(uuid.uuid4())
            title = row.find("a",  attrs = {'class':'result-title hdrlnk'}).text
            time = row.find("time",  attrs = {'class':'result-date'})["datetime"]
            price = row.find("span",  attrs = {'class':'result-price'}).text
            url = row.find("a", href=True)["href"]

            new_entry = cl_listing(id, title, time, price, url)
            listings[id] = new_entry

        page += 120

        for value in listings.values():
            value.print()