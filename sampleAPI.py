#for complete guide refer to API documentation  here https://developers.google.com/books/docs/v1/using 

import requests

url = "https://www.googleapis.com/books/v1/volumes?"

# query to search using isbn
res = requests.get(url, params={ "q": {"isbn:0374528373"} })

print(res.json())

