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
        div_main = soup.find_all('div', attrs=('id';'main'))[0]
        self.data = div_main.find_all('pre')[0]

    def extract_data(self):
        self.data = self.data.text

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self):
        self.get_web()
