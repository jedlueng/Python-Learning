

##### Essentials:

## os
## requests, BeautifulSoup
## re (regex)
## math
## time
## Selenium (automation)
## JSON
# import json
# x = '{ "name":"John", "age":30, "city":"New York"}'

# print(type(x))
# x = json.loads(x)
# print(type(x))
# print(x)



## Pandas, Numpy, SciPy
## Seaborn, MatplotLib

###### Algorithms:

# Stacks, queues
# Binary Trees
# Linked Lists
# Big O Notation
# Leetcode Grind!


###############################
import json
import requests as rq




req_string = 'http://ws1.metcheck.com/ENGINE/v9_0/json.asp?lat=53.3&lon=-1.7&lid=62441&Fc=No'



r_check = rq.get(req_string).status_code
### A function to accept URL:
## Return True if site is ok, False otherwise?

def check(url):
  try:
    if rq.get(url).status_code == 200: 
      return True 
    return False    
  except:
    return False


def get_json_request(url):
  return(json.loads(rq.get(url).text)) 


def main():
  url = 'http://ws1.metcheck.com/ENGINE/v9_0/json.asp?lat=53.1&lon=-3.8&lid=60984&Fc=No'
  if check(url):
    downloaded_data = get_json_request(url)
    data = downloaded_data['metcheckData']['forecastLocation']['forecast'][0]
    today_sunrise = data['sunset']
    print(today_sunrise)
    



# url = 'http://ws1.metcheck.com/ENGINE/v9_0/json.asp?lat=53.3&lon=-1.7&lid=62441&Fc=No'
# downloaded_data = get_json_request(url)
# print(downloaded_data['metcheckData'])

main()