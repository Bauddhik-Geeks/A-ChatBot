from Crypto.PublicKey import RSA
import binascii
import random
import requests
import os

def verfiyKey(key: str):
    try:
        if len(key) < 750:
            return False
        RSA.importKey(binascii.unhexlify(key))
        # .publickey().exportKey('PEM')
        return True
    except:
        return False


# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    return otp


def SendOtp(mail, frm):
    otp=otpgen()
    requests.post(
        "https://api.eu.mailgun.net/v3/account.vote-chain.tech/messages",
        auth=("api", os.environ.get('mailGunAPI')),
        data={"from": "VoteChain verification <{}@account.vote-chain.tech>".format(frm),
              "to": [mail],
              "subject": "Account verification | VoteChain",
              "template": "otpsend",
              "v:otp":otp})
    return otp
Footer
