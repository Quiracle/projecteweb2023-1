import requests
import pprint
import sys
import json

class IPInfo(object):
    def __init__(self) -> None:
        self.url1 = "https://api.ipify.org/?format=json"
        self.url2 = "https://ipinfo.io/"
        self.url2_suffix = "/geo"

    def query_json(self, url):
        resultat = requests.get(url)
        dades = json.loads(resultat.text)
        return dades
    
    def query_myip(self):
        dades = self.query_json(self.url1)
        return dades["ip"]
    
    def query_ipinfo(self, ip):
        dades = self.query_json(self.url2+ip+self.url2_suffix)
        return dades
    
    def get_data(self, query = ""):
        myip = self.query_myip()
        dades = self.query_ipinfo(myip)
        return dades
    

if __name__ == "__main__":
    client = IPInfo()
    if len(sys.argv)>1:
        data = client.get_data(sys.argv[1])
    else:
        data = client.get_data()
    pprint.pprint(data)
