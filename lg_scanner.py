from bs4 import BeautifulSoup
from lg_listing import lg_listing
import requests
import uuid

if __name__ == '__main__':

    page = 1
    listings = {}

    for x in range(0, 3):

        # letgo / electronics / page x / distance = 10 miles / long-lat = basking ridge
        URL = "https://www.letgo.com/en-us/c/electronics/page/" + str(page) + "?distance=10&latitude=40.70661740000001&longitude=-74.54932840000001"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find("div",  attrs = {'data-testid':'feed-grid'})
        for item in table.findAll("div",  attrs = {'class':'sc-AxirZ geclJW'}):

            id = str(uuid.uuid4())
            title = item.find("p",  attrs = {'data-testid':'feed-grid-item-name'}).find("a").text
            price = item.find("p",  attrs = {'data-testid':'feed-grid-item-price'}).find("span").text
            url = "www.letgo.com" + item.find("p",  attrs = {'data-testid':'feed-grid-item-name'}).find("a")["href"]

            new_entry = lg_listing(id, title, price, url)
            listings[id] = new_entry

        page += 1

        for value in listings.values():
            value.print()