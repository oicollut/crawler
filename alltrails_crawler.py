
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from requests.auth import HTTPBasicAuth
import json


def crawler(url):
    session = HTMLSession()
    cookies = {"datadome" : "A27MfPgr5V-hp29MLysid6m2n2l-HUArG80aNQ6fycjrH4b6~MJIm9UC7fYnEYalQSznbWE_0glxzdqS_gQdMl5x5RGhB9gt-BL.OIPU~frSiKCrOBfK.fpTonSJ_-e"}
    headers = {"x-at-key": '3p0t5s6b5g4g0e8k3c1j3w7y5c3m4t8i'}
    r = session.get(url, cookies=cookies, headers=headers)
    result = json.loads(r.html.full_text)
    print(result)

          
crawler("https://www.some-url/api/someapi") #insert your URL

