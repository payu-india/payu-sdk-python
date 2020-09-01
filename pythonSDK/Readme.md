PayU Python Serverside sdk
===================


Python server side sdk to interact with **PayU**[^stackedit]. 
This is primarily for generating hashes at the server to interact with **PayU** for making transaction.

----------
Installation
-------------
```
$pip install payu
```
----------
**Usage**
You need to set up your key and salt values, you can find in your dashboard.

    import payu
    client = payu.payUClient("<key>","<salt>)

Next you have to collect payment params needed to make a payment request e.g.

    params = {"txnid":"202005110207","amount":"10","productinfo":"iPhone","firstname":"userFirstName","email":"email@email.com"}

You can also append user defined values to the params in udfs. e.g.

    params = {"udf1":"street address","udf2":"city","udf3":"zip","udf4":"country","udf5":"some other value"

**Generate Payment Hash**
To get the payment hash you need to call generate_hash function as follows:

    payu.Hasher.generate_hash(params)

**Validate Hash**
After transaction is made, you need to cross-verify the hash to make sure it was not tempered. So, if the hash generated from validate hash matched the reverse_hash(you get after each transaction) that means transaction was not tempered.

    payu.Hasher.validate_hash(params)

> **Note:** Calculation of reverse hash is mandatory and we recommend this to be calculated after each transaction. 



