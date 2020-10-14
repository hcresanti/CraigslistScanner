class cl_listing:

    def __init__(self, id, title, time, price, url):
        self.id = id
        self.title = title
        self.time = time
        self.price = price
        self.url = url

    def print(self):
        print("Title: " + self.title)
        print("  - Price: " + self.price)
        print("  - Date: " + self.time)
        print("  - ID: " + self.id)
        print("  - URL: " + self.url)