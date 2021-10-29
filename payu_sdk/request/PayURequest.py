

import hashlib
from payu_sdk.base import Base
import requests


key = ""
salt = ""

url = "https://test.payu.in/_payment"
headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}



class createRequest:


    def paymentRequest(payload):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]

        response = requests.request("POST", url, data=payload, headers=headers)
        return response









