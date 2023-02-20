import urllib
import xmltodict

class ArxivClient(object):
    def __init__(self) -> None:
        self.url = "https://export.arxiv.org/api/query?start=0&max_results=10&search"
        pass

    def query_arxiv(self, query):
        url_query = urllib.request.urlopen()
        xml_data = url_query.read().decode('utf-8')
        return xml_data


    def get_data(self, query):
        result_arxiv = self.query_arxiv(query)
        pass

if __name__ == "__main__":
    client = ArxivClient():
    dades = client.get_data("transformers")
    print(dades)