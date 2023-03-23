from os import system
from time import sleep
from bs4 import BeautifulSoup
import random
import requests
import os

harf="abcdefghijklmnoprstuvyz"
rakam="0123456789"

karistir=harf + rakam
uzunluk=5
sonuc="".join(random.sample(karistir,uzunluk))

while 1:
    system("cls||clear")
    print("""
    
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|ENZA
                                              
  
  Aralarında Sağlam Hesap
  Vardır İllaki Deneyin 
  
  TG: @dark_enza\n  
    """)
    
    try:
    	menu = (input(" 1- Netflix Cookie\n 2- Netflix Eposta+Şifre\n 3- TikTok Eposta+Şifre\n 4- 8 BallPool Eposta+Şifre\n 5- OnlyFans(Günah xd) Eposta+Şifre\n 6- Çıkış\n\n Seçim: "))
    	if menu == "":
    		continue
    	menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print("Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(2)
        continue
#======== Netflix Cookie =========#
    if menu == 1:
    	system("cls||clear")
    	url="https://tools.1877.to/assets/webfonts/fa-regular-"+sonuc+".ttf"
    	headers1={
    		'Host': 'tools.1877.to',
    	'Cookie':'BlazingPuzzleCookie=m6i3DfrF6gkBgSk2LDLrae4Bpczk90eIXI8dP5IpPmU7mtYha8gB8Hy3R2ZYvZpX; BlazingWebCookie=5mjMTDJyduOz0qAwCypnsRZMN4ekO2b0sD4dx6Gj9g84io34nWIG2YSsK3GpJOUP'
    		}
    	rsp=requests.get(url,headers=headers1, verify=False)
    	
    	veri=BeautifulSoup(rsp.content,"html.parser")
    	netflixcookie=veri.findAll("textarea",class_="form-control")
    	x=(list(map(lambda x:x.text,netflixcookie)))
    	for i in range(2):
    		print("Netflix Cookie Kopyala Kullan")
    		print("")
    		print(x[i])
    		
    	print("\nCookie Yukarıda Verildi Kopyala kullan")
    	print("\nMenüye dönmek için 'enter' tuşuna basınız..")
    	input()
#========= Netflix Email + şifre =========#
    if menu == 2:
    	system("cls||clear ")
    	url="https://tools.1877.to/assets/webfonts/fa-regular-"+sonuc+".ttf"
    	headers1={
    		'Host': 'tools.1877.to',
    	'Cookie':'BlazingPuzzleCookie=m6i3DfrF6gkBgSk2LDLrae4Bpczk90eIXI8dP5IpPmU7mtYha8gB8Hy3R2ZYvZpX; BlazingWebCookie=5mjMTDJyduOz0qAwCypnsRZMN4ekO2b0sD4dx6Gj9g84io34nWIG2YSsK3GpJOUP'
    		}
    	rsp=requests.get(url,headers=headers1, verify=False)
    
    	veri=BeautifulSoup(rsp.content,"html.parser")
    	netflixmail=veri.findAll("section",class_="netflixemailpass")
    	x=(list(map(lambda x:x.text,netflixmail)))
    	for i in range(0,1):
    		sonuc = x[i]
    		with open('hesap.txt', 'w') as a:
    			a.write(str(sonuc))
    	if os.path.isfile('hesap.txt'):
    		with open('hesap.txt', 'r') as r:
    			data = r.readlines()
    			htmlisim = str(data[3])
    			mail = str(data[8])
    			print(htmlisim,"Eposta Şifre: "+mail)
    	print("\nMenüye dönmek için 'enter' tuşuna basınız..")
    	input()
    	
#========= TikTok Epost + Şifre ======#
    if menu == 3:
    	system("cls||clear ")
    	url="https://tools.1877.to/assets/webfonts/fa-regular-"+sonuc+".ttf"
    	headers1={
    		'Host': 'tools.1877.to',
    	'Cookie':'BlazingPuzzleCookie=m6i3DfrF6gkBgSk2LDLrae4Bpczk90eIXI8dP5IpPmU7mtYha8gB8Hy3R2ZYvZpX; BlazingWebCookie=5mjMTDJyduOz0qAwCypnsRZMN4ekO2b0sD4dx6Gj9g84io34nWIG2YSsK3GpJOUP'
    		}
    	rsp=requests.get(url,headers=headers1, verify=False)
    
    	veri=BeautifulSoup(rsp.content,"html.parser")
    	tiktok=veri.findAll("section",class_="tiktok")
    	x=(list(map(lambda x:x.text,tiktok)))
    	for i in range(0,1):
    		sonuc = x[i]
    		with open('hesap.txt', 'w') as a:
    			a.write(str(sonuc))
    	if os.path.isfile('hesap.txt'):
    		with open('hesap.txt', 'r') as r:
    			data = r.readlines()
    			htmlisim = str(data[3])
    			mail = str(data[8])
    			print(htmlisim,"Eposta Şifre: "+mail)
    	print("\nMenüye dönmek için 'enter' tuşuna basınız..")
    	input()
#========= 8 Ball Pool Epost + Şifre ======#
    if menu == 4:
    	system("cls||clear ")
    	url="https://tools.1877.to/assets/webfonts/fa-regular-"+sonuc+".ttf"
    	headers1={
    		'Host': 'tools.1877.to',
    	'Cookie':'BlazingPuzzleCookie=m6i3DfrF6gkBgSk2LDLrae4Bpczk90eIXI8dP5IpPmU7mtYha8gB8Hy3R2ZYvZpX; BlazingWebCookie=5mjMTDJyduOz0qAwCypnsRZMN4ekO2b0sD4dx6Gj9g84io34nWIG2YSsK3GpJOUP'
    		}
    	rsp=requests.get(url,headers=headers1, verify=False)
    
    	veri=BeautifulSoup(rsp.content,"html.parser")
    	miniclip=veri.findAll("section",class_="miniclip")
    	x=(list(map(lambda x:x.text,miniclip)))
    	for i in range(0,1):
    		sonuc = x[i]
    		with open('hesap.txt', 'w') as a:
    			a.write(str(sonuc))
    	if os.path.isfile('hesap.txt'):
    		with open('hesap.txt', 'r') as r:
    			data = r.readlines()
    			htmlisim = str(data[3])
    			mail = str(data[8])
    			print(htmlisim,"Eposta Şifre: "+mail)
    	print("\nMenüye dönmek için 'enter' tuşuna basınız..")
    	input()

#======== Only Fans Eposta+Şifre =======#
    if menu == 5:
    	system("cls||clear ")
    	url="https://tools.1877.to/assets/webfonts/fa-regular-"+sonuc+".ttf"
    	headers1={
    		'Host': 'tools.1877.to',
    	'Cookie':'BlazingPuzzleCookie=m6i3DfrF6gkBgSk2LDLrae4Bpczk90eIXI8dP5IpPmU7mtYha8gB8Hy3R2ZYvZpX; BlazingWebCookie=5mjMTDJyduOz0qAwCypnsRZMN4ekO2b0sD4dx6Gj9g84io34nWIG2YSsK3GpJOUP'
    		}
    	rsp=requests.get(url,headers=headers1, verify=False)
    
    	veri=BeautifulSoup(rsp.content,"html.parser")
    	onlyfns=veri.findAll("section",class_="onlyfans")
    	x=(list(map(lambda x:x.text,onlyfns)))
    	for i in range(0,1):
    		sonuc = x[i]
    		with open('hesap.txt', 'w') as a:
    			a.write(str(sonuc))
    	if os.path.isfile('hesap.txt'):
    		with open('hesap.txt', 'r') as r:
    			data = r.readlines()
    			htmlisim = str(data[3])
    			mail = str(data[8])
    			print(htmlisim,"Eposta Şifre: "+mail)
    	print("\nMenüye dönmek için 'enter' tuşuna basınız..")
    	
    elif menu == 6:
        system("cls||clear")
        print("Çıkış yapılıyor...")
        break
