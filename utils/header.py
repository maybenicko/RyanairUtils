import random


def headers():
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    ]

    header = {
        "User-Agent": random.choice(user_agent_list),
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7",
        "client": "desktop",
        "client-version": "3.132.0",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": 'mkt=/it/it/; STORAGE_PREFERENCES={"STRICTLY_NECESSARY":true,"PERFORMANCE":false,"FUNCTIONAL":false,"TARGETING":false,"SOCIAL_MEDIA":false,"PIXEL":false,"__VERSION":3}; RY_COOKIE_CONSENT=true; agsd=MoHIiaPpLocbQTQ9BOPi0SfpCDaWZ-wqOvkRQ7KGTxJWvpOq; _cc-x=MTkxODY4NjctZDc2OC00MjI1LTk0NjItODdhNzQwYWEzM2Y2OjE3MjI4ODYzOTIzMTI; _cc=Abg2ihE6yPC83yuR85tCUQ9x; _cid_cc=Abg2ihE6yPC83yuR85tCUQ9x; rid=81748a56-3615-4f52-993c-b81bc181a667; fr-correlation-id=3b6980e5-ed29-4462-8ebd-aea5e81a7811; rid.sig=jyna6R42wntYgoTpqvxHMK7H+KyM6xLed+9I3KsvYZaVt7P36AL6zp9dGFPu5uVxaIiFpNXrszr+LfNCdY3IT3oCSYLeNv/ujtjsDqOzkY5JmUFsCdAEz3kpPbhCUwiArp5oaa75tpJtO3kFwYQ8l0DbH67AtcN/PMbniLsiM5qn+2AjrrtoNJicE3ZQwFHVipe4lWPSRfq2OIyUrlFhwEDt20+wCX7l1mCubNXtG6nZrUA07sFUFhn4RUxnjwjJ6d9qjjBasXLvYSqyYN7UadcxLyXgua2mbG5A40mHEBkbUFX7tZUe/2eTn3M9vR4+kyMtsPHs0WKVAIVTBOqQw9zt0F7h7SmB+5XmFQCA5TTuWKPMdsI8mf8zuExhccNdbGYlWftWuU+ly/w6ykLFa/A8KvO3JH+BLCNT9nisWbO/9lV4yaWSKjnEXPgZP6154ZxTVFjqahc67BznTGdZ/3Q8YgUReCvaxUrg8RvYspn0yQ1EQ4F4IHzt0MSQH9MlDjDIlsmvKiNxAb/5icbLIfSKOBs05qR24QpVPcCfWbJefDrbKqeoW6SePz7fm2lHW2pfgQFEGle3bPZ2HtkFs8tXM+DjPGDG2FuldQv98vnhpNp3V8PYz8AXioVsjyGVmzrl8WfKM1q8H1v8sDlonGxIYQIVyKtW5LCG3Gjk6eTEpuMl69wF3erM7OVSe3s3saY5wECp8uRmh4in7HaffOdBETe9vidRWSjsiU+RLTxIGdBpvsBoymT4KbvEPsGFzDHfVHLNrONIEpRAeQZZwDXKrDEeqo5B8173No7bnJieUbn2smoKmPIvgQSmHgXW42stZZ0icHb67C94bil8eitV0A9CeAeu4sF0/polq50O99nr3pUuYKCGk6yQqWrHRlT8HUq1+COhrjbNO54qCT/CEHEtuO1KTvCTAJS5XAaIoozkGqtJFrVi6C8udQonS96Quy5gpgc8uL4PjCHs1PZZaFjFAeVyyu1PNNZA6SbhVNh2lPeHI5AgP59BcU+DVMHvDXPHBfQUPkiG0Oc3aWdEDOCyWMNLqmUWNeuYoJTO3Gum3iR1SKyFE+ukqmlMtuAl9SHiZ6mbnFFgUcJA62o/73TSfTGeJPUEu/J/1Fv2F1MIxFA3PAE9WPbnTxwHMgHxWxUw1qBT/Blo/5xki6U8FEXO61SIIDexqHkwQ5U99WIdUAEapke16b/U/8MN7pyd1vRZKX2ErQ8hbRoUTQ=='
    }
    return header