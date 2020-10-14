class lg_listing:

    def __init__(self, id, title, price, url):
        self.id = id
        self.title = title
        self.price = price
        self.url = url

    def print(self):
        print("Title: " + self.title)
        print("  - Price: " + self.price)
        print("  - ID: " + self.id)
        print("  - URL: " + self.url)