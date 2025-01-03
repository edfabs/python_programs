from urllib.request import urlopen
url = "https://es.wikipedia.org/wiki/Segunda_guerra_angloneerlandesa"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)