import pyshorteners
def urlShortener(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
url = input("Enter the URL : ")
urlShortener(url)