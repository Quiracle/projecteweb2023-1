import urllib3
import bs4

class WebScrape(object):
    def __init__(self) -> None:
        self.url = "https://www.99-bottles-of-beer.net/language-python-808.html"
    
    def get_web(self):
        httppool = urllib3.PoolManager()

        resposta = httppool.request("GET", self.url)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features = "html.parser")
        div_main = soup.find_all("div", attrs=("id";"main"))

    def parse_html(self):
        self.parse_bs4()

    def get_data(self):
        self.get_web()
