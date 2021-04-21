import requests,sys,colorama
from colorama import *
init(autoreset=True)


def verify():
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
	poc=urls

	try:
		requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
		response=requests.get(poc,headers=headers,timeout=5,verify=False)
		if response.status_code==404 and "There isn't a GitHub Pages site here." in response.text:
			print('{} is  vulnerability'.format(urls))
			# print(response.content)
			#将漏洞地址输出在Vul.txt中
			f=open('./vul.txt','a')
			f.write(urls)
			f.write('\n')
		else:
			print('{} None'.format(urls))
	except:
		print('{} request timeout'.format(urls))

if __name__ == '__main__':

	if len(sys.argv)!=2:
		print('Example:python CVE-2017-16894.py urls.txt')
	else:
		file = open(sys.argv[1])
		for url in file.readlines():
			urls=url.strip()
			if urls[-1]=='/':
				urls=urls[:-1]
			verify()
		print ('Check Over')



