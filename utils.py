from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json


URL='https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Diego%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-117.282538%2C%22east%22%3A-116.90816%2C%22south%22%3A32.534857%2C%22north%22%3A33.114249%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54296%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22isMapVisible%22%3Afalse%7D&includeMap=false&includeList=true'

def cookie_parser():
    cookie_string='zguid=23|%246357d797-c41c-4518-99bf-418c1b61ef8c; _ga=GA1.2.1019427332.1584684752; _pxvid=c826cbe3-6a71-11ea-aa45-0242ac12000b; zjs_user_id=null; zjs_anonymous_id=%226357d797-c41c-4518-99bf-418c1b61ef8c%22; _gcl_au=1.1.75950928.1584684754; _fbp=fb.1.1584684754632.698330712; __gads=ID=bd1953a279722338:T=1584685340:S=ALNI_MYC1jYeTR-y5nWH2L2sH-0G1X8QHQ; ki_r=; ki_s=199442%3A0.0.0.0.0; zgsession=1|f4a79734-6b56-402f-adc4-db06c93d1309; _gid=GA1.2.1334535751.1591865131; KruxPixel=true; DoubleClickSession=true; _pin_unauth=dWlkPU5XRmpZemc1TURFdFpHVXlOeTAwTVdGbExUbGlNakF0T1RGaE56azVNRGhrWW1KaA; KruxAddition=true; FSsampler=1172229883; JSESSIONID=ABEB9F5C6BA03FC9A8848B0D7742E7C3; _gat=1; GASession=true; _uetsid=55a5d631-8f5e-55fe-4f79-fe52ebda92ee; _uetvid=59142f87-c7db-50b6-f0c0-7f8f70ee319b; _px3=1eeff9a4e75475f200601fb1f6ad94e6a71ab8c6c2d1c02057c250d42a72fcdb:2cRMUO4Uyndf4x49GFAaSqD8t9nrkmWdtO6rQs++u867V8TR33WXLkI92Zi9DWWYT1l6dwT4Lqc4bKt1oz9yvQ==:1000:cCFIvjFBJ+BGpSXBOJn+DkKSSz7w1hl3HPzgZ+45uxUA074Zpfr8cgj2G4/8utrt5zvmnVY3YoFeP/TCcopGmwVd/8CrN6GkKpMwJ1pGvgNDRsZg+MYsSuW9tYoenj0K7bfd9XycHKfht5qijqbWwY+3SVenMEsU3opNYN9Qybc=; AWSALB=7dofm3L8iZoVSS8XBoAZLAXMsdhK4beAObiWXX7MBq1cdBb4BX96XyHWV+1uelHdBBQLHVYo2bNWxxJa5LD8Z/0TWYZ9jia9IURH92OWZZnBl+ZESzBMX52x3M8l; AWSALBCORS=7dofm3L8iZoVSS8XBoAZLAXMsdhK4beAObiWXX7MBq1cdBb4BX96XyHWV+1uelHdBBQLHVYo2bNWxxJa5LD8Z/0TWYZ9jia9IURH92OWZZnBl+ZESzBMX52x3M8l; search=6|1594480525132%7Crect%3D33.114249%252C-116.90816%252C32.534857%252C-117.282538%26rid%3D54296%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0954296%09%09%09%09%09%09; ki_t=1584685344640%3B1591865196489%3B1591888531312%3B2%3B412'

    cookie=SimpleCookie()
    cookie.load(cookie_string)
    # print(cookie.items())
    # first we get back tuple of cookies, then we loop through the tuples and get back a dict
    
    cookies={}

    for key, morsel in cookie.items():
        cookies[key]= morsel.value

    

    return cookies
#cookie_parser()

def parse_new_url(url, page_number):
    url_parsed=urlparse(url)
    #print(url_parsed.query)
    query_string=parse_qs(url_parsed.query)
    #print(query_string)
    #convert from string to dict= json.loads()
    search_query_state=json.loads(query_string.get('searchQueryState')[0])
    #print(search_query_state)
    search_query_state['pagination']= {"currentPage":page_number}
    #print(search_query_state)
    query_string.get('searchQueryState')[0]= search_query_state
    #print(query_string)
    #we need to set doseq 1 so that ouput will not be converted to list and break later
    encoded_qs= urlencode(query_string, doseq=1)
    new_url= f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    #print(new_url)
    return new_url
    


#parse_new_url(URL, 6)
    


