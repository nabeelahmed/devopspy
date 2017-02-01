from elasticsearch import Elasticsearch
import requests
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

response = requests.get('http://localhost:9200') 
i = 1
while response.status_code == 200: # runs until get a 404 i.e. not found
    response = requests.get('http://swapi.co/api/planets/'+ str(i)) 
    es.index(index='swapi', doc_type='planets', id=i, body=json.loads(response.content))
    i=i+1
 
print"indexed ",i, " Planets to ES"

