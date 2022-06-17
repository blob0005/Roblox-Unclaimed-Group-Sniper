try:
    import os
    from os import system
    system("title " + "Roblox Unclaimed Group Sniper,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
anyerror = False
try:
    import requests
    import colorama
except:
    anyerror = True
if anyerror == True:
    autfix = input("Missing Modules, Wanna Try Auto Fix (y/n): ")
    if autfix == "n":
        exit()
    if autfix == "y":
        try:
            import os
            os.system("pip install colorama")
            os.system("pip install requests")
            print("Problem May Be Fixed Now, Restart The Program")
            input("")
            exit()
        except:
            print("Error While Fixing, Press Enter To Exit Program")
            input("")
            exit()
import random, time, threading
try:
    import os
    from os import system
    system("title " + "Roblox Unclaimed Group Sniper,   Made By blob#0005,    Github: github.com/blob0005")
except:
    pass
colorama.init(autoreset=True)
def sniper():
    try:
        while True:
            if wannarange == "n":
                groupid = random.randint(1, 15000000)
            if wannarange == "y":
                groupid = random.randint(rangeA, rangeB)
            groupid = str(groupid)
            id = str(groupid)
            r = requests.get("https://www.roblox.com/groups/group.aspx?gid="+str(groupid)).text
            r = str(r)
            if "owned" not in r:
                r2 = requests.get(f"https://groups.roblox.com/v1/groups/"+groupid)
                if "isLocked" not in r2.text and "owner" in r2.text:
                    entry = r2.json()["publicEntryAllowed"]
                    owner = r2.json()["owner"]
                    if entry == True and owner == None:
                        print(colorama.Fore.GREEN + "Valid Group! https://roblox.com/groups/"+id)
                        if save == "y":
                            validfile = open("valid_groups.txt", "a")
                            validfile.write("https://roblox.com/groups/"+id+"\n")
                            validfile.close()
                        try:
                            r = requests.post(webhook, json={"content": "@here **Sniper Group** https://roblox.com/groups/"+id})
                        except:
                            pass
                else:
                    print(colorama.Fore.RED + "Invalid Group! https://roblox.com/groups/"+id)
                    if save == "y":
                        invalidfile = open("invalid_groups.txt", "a")
                        invalidfile.write("https://roblox.com/groups/"+id+"\n")
                        invalidfile.close()
            else:
                print(colorama.Fore.RED + "Invalid Group! https://roblox.com/groups/"+id)
                if save == "y":
                    invalidfile = open("invalid_groups.txt", "a")
                    invalidfile.write("https://roblox.com/groups/"+id+"\n")
                    invalidfile.close()
            time.sleep(float(delay))
    except:
        print(colorama.Fore.RED + "Unkown Error")
while True:
    try:
        threads = input("Enter How Many Threads (If To Many Printing The Codes Will Get Laggy): ")
        threads = int(threads)
        break
    except:
        print("Enter A Valid Choice")
while True:
    try:
        delay = input("Enter Delay For Each Thread (0 = None): ")
        delay = float(delay)
        break
    except:
        print("Enter A Valid Chioce")
webhook = input("Enter Webhook (Leave Blank For None): ")
while True:
    save = input("Wanna Auto Save All Groups (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        print("Enter A Valid Choice")


while True:
    wannarange = input("Wanna Pick Range (y/n, Advanced Option): ")
    if wannarange == "y" or wannarange == "n":
        break
    else:
        print("Enter A Valid Choice")


if wannarange == "y":
    while True:
        try:
            rangeA = input("What Shall The Minimum Range Be: ")
            rangeA = int(rangeA)
            break
        except:
            print("Enter A Valid Chioice")
    while True:
        try:
            rangeB = input("What Shall The Maximum Range Be: ")
            rangeB = int(rangeB)
            break
        except:
            print("Enter A Valid Chioice")
    

try:
    for u in range(int(threads)):
        t1 = threading.Thread(target=sniper)
        t1.start()
except Exception:
    print("Unkown Error")
    input("")
    exit()
