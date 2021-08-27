import requests
from win10toast import ToastNotifier
import json
import time
def update():
    craw=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=craw.json()
    text=f'Cases:{data["cases"]}\nDeath:{data["deaths"]}\nRecovered:{data["recovered"]}'
    while True:
        t=ToastNotifier()
        t.show_toast("Covid Update",text,duration=20)
        time.sleep(60)
update()
