#!/usr/bin/env python
import requests

url = 'http://0.0.0.0:6007/simulate'
lines = open('train-small.json').read().split("\n")
for data in lines:
  response = requests.post(url, data=data, headers={"Content-Type": "application/json"})
  print(response.text)
