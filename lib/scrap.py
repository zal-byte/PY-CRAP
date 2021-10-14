from bs4 import BeautifulSoup as BS
from requests import get
class Crap( object ):
    def __init__(self):
        self.tag = None
        self.attr = None
        self.url = "https://qeevdev.code.blog"
    def scrap(self):
        bs = BS( self.content(), "html5lib")
        find_all = bs.find_all( "a", attrs={"rel":"bookmark"} )
        return find_all;
    def content(self):
        r = get(self.url)
        return r.text