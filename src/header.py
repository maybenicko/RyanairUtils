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
        "cookie": 'mkt=/it/it/; STORAGE_PREFERENCES={"STRICTLY_NECESSARY":true,"PERFORMANCE":false,"FUNCTIONAL":false,"TARGETING":false,"SOCIAL_MEDIA":false,"PIXEL":false,"__VERSION":3}; RY_COOKIE_CONSENT=true; agsd=MoHIiaPpLocbQTQ9BOPi0SfpCDaWZ-wqOvkRQ7KGTxJWvpOq; _cc-x=MTkxODY4NjctZDc2OC00MjI1LTk0NjItODdhNzQwYWEzM2Y2OjE3MjI4ODYzOTIzMTI; _cc=Abg2ihE6yPC83yuR85tCUQ9x; _cid_cc=Abg2ihE6yPC83yuR85tCUQ9x; rid=81748a56-3615-4f52-993c-b81bc181a667; fr-correlation-id=3b6980e5-ed29-4462-8ebd-aea5e81a7811; rid.sig=jyna6R42wntYgoTpqvxHMK7H+KyM6xLed+9I3KsvYZaVt7P36AL6zp9dGFPu5uVxaIiFpNXrszr+LfNCdY3IT3oCSYLeNv/ujtjsDqOzkY5JmUFsCdAEz3kpPbhCUwiArp5oaa75tpJtO3kFwYQ8l0DbH67AtcN/PMbniLsiM5qn+2AjrrtoNJicE3ZQwFHVipe4lWPSRfq2OIyUrlFhwEDt20+wCX7l1mCubNXtG6nZrUA07sFUFhn4RUxnjwjJ6d9qjjBasXLvYSqyYN7UadcxLyXgua2mbG5A40mHEBkbUFX7tZUe/2eTn3M9vR4+kyMtsPHs0WKVAIVTBOqQw2q6qPayJgsSo6JRwxnBe19JfdYMWzxwfTi+VsZhHm1sBjQYyeOB0d02QHUJLyQgYVUZP9Uf8Ir3S+Uc2H+v3DHuVNGNcKQze2kEpceU0hmlcE7CLPbgVYMGYwS5AjxPxboeLevIqLoIdyVrAjuTWpqhmvpJoJ8ChBGhQDIdPcaWktDX8/L4U78SD4UUCWmnObhSs8IPxPDC7qnKGPSsQGjUbKUpElGcxQRreMD6II/bAIaz2XIgm8Kzinw+f7PzStm0XmS4Nvu5iWpyUQHHd2CFJ5v7jClPIWZ0fKV5gZ28PTeolaCjiBZhS+OO22ipofvUsmZtlrtqLz30l4WInyYja0ywWZJtm4eeTaDvJ4Q2/Q+NNjUEg5wKdq6s/etWRwDaXxxk47Ds54LWh79l0TIJcZZZDioYic8QYXxWX4DcVtEYEszO33RV1gSD08JsrtA9y9Lkl+SJFdNm+VdYRY0dybptm1rLQZfMMuigwA8qfZJFrXm6dTf7OmzbzFtSpXVf8sIZ6nAUVQjHfpqBTOZshbW/GPJ5EUIiK1aoV2FOuhBcXNpBiAxjYC1H26OMd2toFyqboT2jpt7OA1INAPjBCzoMq93XuoaTbg5OMGP5sWvTOGjeqHt1G4RmiEx/zXpgis+b22jdXnREgBIEb0mIEJZslwRgwKS85vfk65xWVSODX/pSh5o1aew4FP36vl1U5CljDAxxZzslIxZVCJvOMFFPFEgKH5OeCJ22v0A0zpI10oSfMmJNzWPJ4HpO3xogl8vI+ovPJeqG1ZfpZxeQC7R6N4DKNOqxi1KvpaITeU75P4feTi8sT1l/wjHI6Xm2iFkSsBYiHNfJrlEFeKk9qzWICMdLOt3Rt4PsXwxA2mGEwhxKToVio3ndwF1ZwsnbH9llwJtbLHvQR8mw2mowxV+3hH/d6z3KWGcWY7VV'
    }
    return header