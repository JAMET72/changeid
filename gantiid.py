import requests, json, time, os, sys, random
from time import sleep

green = '\033[1;32m'
red ='\33[31;1m'
white = '\33[37;1m'

def mengetik(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(random.random() * 0.1)
sleep(0.1)

API_BASE_URL = "https://id-api.spooncast.net"
API_LOGIN = '/signin/'
API_USER = '/users/'
API_IDCHANGE = 'username/'
paramex = {'cv':'heimdallr'}
def id():
	nomerhp = input("Masukan No Telfon : ")
	passwordhp = input("Kata Sandi : ")
	sleep(1)
	mengetik('''
Loading . . . 
█ █ █ █ █ █ █ █ 1 0 0 %      
''')
	os.system('clear')
	headers1={'User-Agent':'Spoon/4.3.22(203) Dalvik/2.1.0 (Linux; U; Android 9; Redmi 4X Build/PQ2A.190305.002'}
	auth = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
	r = requests.post(API_BASE_URL + API_LOGIN ,headers=headers1, json=auth)
	respon_data = r.json()
	for i in respon_data['results']:
		taguser = i['id']
		tokennyaa = i['token']
		idbaru = input('New ID: ')
		os.system('clear')
		inputidbaru = {'username':idbaru}
		headers = {'Authorization':'Token ' + tokennyaa,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		"origin":"https://www.spooncast.net",
		"referer":"https://www.spooncast.net/",
		'content-type':'application/json',
		'User-Agent':'AppleWebKit/537.36 Mozilla'}
		rid = requests.post(API_BASE_URL + API_USER + API_IDCHANGE,headers=headers,params=paramex,json=inputidbaru)
		if rid.status_code == 200:
			print(green,'\nBerhasil Cek ID Baru Kamu ! ' +white+ str(idbaru))
			print(red,'\JAMET')
		elif rid.status_code == 400:
			print(red,'\nForbidden ! Your ID is taken or invalid.')
			#print('Silahkan Cek ID Spoon kamu.')
id()
