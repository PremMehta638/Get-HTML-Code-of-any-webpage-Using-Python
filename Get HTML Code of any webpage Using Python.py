# Improting the required module
import requests

r = requests.get("https://google.com")
print (r.text)