



import hashlib
from payu_sdk.base import Base
import requests

key = ""
salt = ""
url = "https://test.payu.in/merchant/postservice?form=2"
headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

class verifyPayment:

    def verifyPaymentStatusByTransactionID (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response


    def verifyPaymentStatusByPayUID (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



''' 
 This API is used to check the status of refund/cancel requests. 
 Whenever the cancel_refund_transaction API is executed successfully, a request ID is returned in the output parameters for that particular request, 
 var1 is Request ID which is returned in the output parameters for that particular request. 
 
 '''
class RefundAPI:

    def refundTransaction (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response




class BinAPI:

    def fetchCardDetailsByBIN (params):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]

        response = requests.request("POST", url, data=params, headers=headers)
        return response


'''

This API is used to check the status of an offer for a particular merchant when all the details are passed.
The return parameters are status, msg, discount/error_code, category, offer_key, offer_type(instant/ cashback) , 
offer_availed_count, offer_remaining_count.
'''

class OffersAPIs:

    def CheckOfferStatusByCategoryAndCardNumber(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response























