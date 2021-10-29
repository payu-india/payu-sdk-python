import os
import json
import pkg_resources

from payu_sdk.base import Base

class payUClient:

    key = ""
    salt = ""

    def __init__(self, credes):
        self.key = credes.get("key")
        self.salt = credes.get("salt")
        client = Base()
        client.set_params(credes)






