import hashlib
from payu.base import Base

key = ""
salt = ""

class Hasher:



    def generate_hash(params):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]
        txnid = params.get("txnid")
        amount = params.get("amount")
        productinfo = params.get("productinfo")
        firstname = params.get("firstname")
        email = params.get("email", "default")
        udf1 = params.get("udf1", "")
        udf2 = params.get("udf2", "")
        udf3 = params.get("udf3", "")
        udf4 = params.get("udf4", "")
        udf5 = params.get("udf5", "")
        if params.get("additional_charges") is True:
            additional_charges = params.get("additional_charges")
            payment_hash_sequence = f"{additional_charges}|{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
        else:
            payment_hash_sequence = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"

        hash_value = hashlib.sha512((payment_hash_sequence).encode('utf-8')).hexdigest().lower()
        return hash_value
'''Response received from Payment Gateway at this page.
It is absolutely mandatory that the hash (or checksum) is computed again after you receive response from PayU and compare it with request and post back parameters. This will protect you from any tampering by the user and help in ensuring a safe and secure transaction experience. It is mandate that you secure your integration with PayU by implementing Verify webservice and Webhook/callback as a secondary confirmation of transaction response.

Hash string without Additional Charges -
hash = sha512(SALT|status||||||udf5|||||email|firstname|productinfo|amount|txnid|key)

With additional charges - 
hash = sha512(additionalCharges|SALT|status||||||udf5|||||email|firstname|productinfo|amount|txnid|key)
   ''' 
    
    def validate_hash(params):
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]
        txnid = params.get("txnid")
        amount = params.get("amount")
        productinfo = params.get("productinfo")
        firstname = params.get("firstname")
        email = params.get("email", "default")
        udf1 = params.get("udf1", "")
        udf2 = params.get("udf2", "")
        udf3 = params.get("udf3", "")
        udf4 = params.get("udf4", "")
        udf5 = params.get("udf5", "")

        if params.get("additional_charges") is True:
            additional_charges = params.get("additional_charges")
            validate_hash_sequence = f"{additional_charges}|{salt}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"
        else:
            validate_hash_sequence = f"{salt}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"

        validate_hash = hashlib.sha512((validate_hash_sequence).encode('utf-8')).hexdigest().lower()
        return validate_hash
