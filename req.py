#Request modulefor HTTP requests
import requests
r= requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)
#post request: it has an end point and we have to send some data with that
url= "www.something.com"
data= {"p1": 4, 
        "p2": 6}

r2= requests.post(url= url, data=data)
