from color import *
from check_module import *

'''

Turkish Menu

'''

def TR_menu():
    check_internet()
    print('Hosgeldiniz\nAciliyor...')
    print(f"{blue}\n\t\t\t[1]{blue} IP Tracker\n\t\t\t{blue}[2]{blue} Emegi Gecenler\n")
    casualFont()
    secim = str(input(":  "))
    if secim == "1":
        print(F"{green}Baslatiliyor...{green}")
        TR_ip()
    elif secim == "2":
        emegiGecenler()

    elif secim == "exit" or secim == "E":
            secim = str(input("Emin misiniz?:   "))
            if(secim == "y" or secim == "Y" ):
                print("Cikis yapiliyor...")
                exit()
            elif (secim == "n" or secim == "N" ):
                print("Geri donuluyor...")
                TR_menu()        
    else:
        print(F"{red}Yanlis Deger Girdiniz .{red}")
        TR_menu()

def casualFont():
    print(normal)

def emegiGecenler():
    print(f"{green} Yapimci: ir0n{green}\n {blue}Destekleyenler: Apeli07 {normal}")
    secim = str(input("Geriye donmek istermisiniz?(1=Geri, 2=Cikis):  "))
    if secim == "1":
        TR_menu()
    elif secim == "2":
        print("Cikis yapiliyor...")
        exit()
    else:
        print('Yanlis deger girdiniz .')
        emegiGecenler_Reset()

def emegiGecenler_Reset():
    secim = str(input("Geriye donmek istermisiniz?(1=Geri, 2=Cikis):  "))
    if secim == "1":
        TR_menu()
    elif secim == "2":
        print("Cikis yapiliyor...")
        exit()
    else:
        print('Yanlis Deger girdiniz .')
        emegiGecenler_Reset()

def check_internet():
    timeout = 5.
    url = "https://www.google.com/"
    
    try:
        request = requests.get(url, timeout = timeout)
        print(f"{green} [ + ] Internet Bagli. {green}")
        
    except (requests. ConnectionError, requests. Timeout) as exception:
        print(f"{red} [ - ] Internet Baglantinizi Kontrol Ediniz Lutfen. {red}")
        casualFont()
        exit()

def TR_ip():
    try:
        ip = str(input(f"{cyan}Ip adresi:  "))
        casualFont()
        url = ("http://ipwhois.app/json/" + ip)
    
        requestIP = requests.get(url)
        contentIP = requestIP.content 
        data = requestIP.json()
        country = data["country"]
        ipType = data["type"]
        isp = data["isp"]
        countryCode = data["country_code"]
        bolge = data["continent"]
        bolgeCode = data["continent_code"]
        baskent = data["country_capital"]
        tel_code = data["country_phone"]
        dolarKur = data["currency_rates"]
        money = data["currency"]
        moneyCode = data["currency_code"]
        moneySymbol = data["currency_symbol"]
        city = data["city"]
        enlem = data["latitude"]
        boylam = data["longitude"]
        zamanzone = data["timezone"]
        zamandilimi = data["timezone_name"]
    
        print(F'''

            IP: {blue}{ip}{blue}{normal}
            ÜLKE: {country}
            İP Tipi: {ipType}
            BÖLGE KODU: {bolgeCode}
            ÜLKE KODU: {countryCode} 
            BAŞKENTİ: {baskent}
            ÜLKE TELEFON KODU: {tel_code}
            ŞEHİR: {city}
            BÖLGE: {bolge}
            ENLEM: {enlem}
            BOYLAM: {boylam}
            ISP: {isp}
            ZAMAN KUŞAĞI: {zamanzone}
            ZAMAN DİLİMİ: {zamandilimi}
            PARA BİRİMİ: {money} 
            PARA SEMBOLU: {moneySymbol}
            ÜLKEDEKİ DOLAR KURU: {dolarKur}

            ''')
        saveIPinformation = str(input(f"{cyan}Bilgileri kaydetmek istermisiniz ?{cyan}:  "))
        casualFont()
        if saveIPinformation == "e" or saveIPinformation == "E":
            with open("ip.txt",'a', encoding="utf-8") as ipdosya:
                ipdosya.write(f"        IP: {ip}\n        ÜLKE: {country}\n        İP Tipi: {ipType}\n        BÖLGE KODU: {bolgeCode}\n        ÜLKE KODU: {countryCode}\n        BAŞKENTİ: {baskent}\n        ÜLKE TELEFON KODU: {tel_code}\n        ŞEHİR: {city}\n        BÖLGE: {bolge}\n        ENLEM: {enlem}\n        BOYLAM: {boylam}\n        ISP: {isp}\n        ZAMAN KUŞAĞI: {zamanzone}\n        ZAMAN DİLİMİ: {zamanzone}\n        PARA BİRİMİ: {money}\n        PARA SEMBOLU: {moneySymbol}\n        ÜLKEDEKİ DOLAR KURU: {dolarKur}")
        elif saveIPinformation == "h" or saveIPinformation == "H":
            print("Bilgiler Kaydedilmedi.")
            secim = str(input(f"{cyan}Menüye geri dönmek istermisiniz? (E= Evet/H= Hayir):  "))
            if secim == "e" or secim == "E":
                TR_menu()
            elif secim == "h" or secim == "H":
                print("Cikis yapiliyor...")
                exit()
            else:
                print(f"{red}[ - ] Yanlis Deger!")
                exit()
    except:                                             
        print(F"{red}[ - ] Yanlis deger girdiniz .")
        casualFont()
        TR_ip()        

'''
English Language
'''
def EN_menu():
    '''
    There is menu. Menu is easier to our works.

    '''
    EN_check_internet()
    print('Welcome\nStarting...')
    try:
        print("██╗██████╗░░░░░░░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░\n██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗\n██║██████╔╝█████╗░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝\n██║██╔═══╝░╚════╝░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗\n██║██║░░░░░░░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║\n╚═╝╚═╝░░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝\n\t\t\t\tir0n")
        print(f"{blue}\n\t\t\t[1]{blue}IP Tracker\n\t\t\t{blue}[2]{blue}Who contributed \n")
        casualFont()
        secim = str(input(":  "))
        if secim == "1":
            print(F"{green}Starting...{green}")
            EN_ip()
        elif secim == "2":
            EN_emegiGecenler()

        elif secim == "exit" or secim == "e":
            secim = str(input("Are you sure?:   "))
            if(secim == "y" or secim == "Y" ):
                print("Exiting...")
                exit()
            elif (secim == "n" or secim == "N" ):
                print("Returning...")
                EN_menu()
            
        else:
            print(F"{red}You entered the wrong value.{red}")
            EN_menu()
    except Exception:
        print(F"{red}You entered the wrong value.{red}")
        exit()

def casualFont():
    print(normal)

def EN_emegiGecenler():
    print(f"{green} Creator: ir0n{green}\n {blue}Supporters: Apeli07 {normal}")
    secim = str(input("Do you want to go back?(1=Back, 2=Exit):  "))
    if secim == "1":
        EN_menu()

    elif secim == "2":
        print("Exiting...")
        exit()

    else:
        print("You entered the wrong value. just (Y/N)")
        EN_emegiGecenler_Reset()

def EN_emegiGecenler_Reset():
    secim = str(input("Do you want to go back?(1=Back, 2=Exit):  "))
    if secim == "1":
        EN_menu()

    elif secim == "2":
        print("Exiting...")
        exit()

    else:
        print("You entered the wrong value. just (Y/N)")
        EN_emegiGecenler_Reset()


def EN_check_internet():
    timeout = 5.
    url = "https://www.google.com/"
    
    try:
        request = requests.get(url, timeout = timeout)
        print(f"{green} [ + ] Connected to the Internet. {green}")
        
    except (requests. ConnectionError, requests. Timeout) as exception:
        print(f"{red} [ - ] Please Check Your Internet Connection. {red}")
        casualFont()
        exit()

def EN_ip():
    try:
        ip = str(input(f"{cyan}Ip address:  "))
        casualFont()
        url = ("http://ipwhois.app/json/" + ip)
        
        requestIP = requests.get(url)
        contentIP = requestIP.content 
        data = requestIP.json()
        country = data["country"]
        ipType = data["type"]
        isp = data["isp"]
        countryCode = data["country_code"]
        bolge = data["continent"]
        bolgeCode = data["continent_code"]
        baskent = data["country_capital"]
        tel_code = data["country_phone"]
        dolarKur = data["currency_rates"]
        money = data["currency"]
        moneyCode = data["currency_code"]
        moneySymbol = data["currency_symbol"]
        city = data["city"]
        enlem = data["latitude"]
        boylam = data["longitude"]
        zamanzone = data["timezone"]
        zamandilimi = data["timezone_name"]

        
        print(F'''

            IP: {blue}{ip}{normal}
            COUNTRY: {country}
            IP TYPE: {ipType}
            REGION CODE: {bolgeCode}
            COUNTRY CODE: {countryCode} 
            CAPITAL: {baskent}
            COUNTRY PHONE CODE: {tel_code}
            CITY: {city}
            REGION: {bolge}
            LATITUDE: {enlem}
            LONGITUDE: {boylam}
            ISP: {isp}
            TIME ZONE: {zamanzone}
            TIME PERIOD: {zamandilimi}
            CURRENCY: {money} 
            CURRENCY SYMBOL: {moneySymbol}
            CURRENCY RATES: {dolarKur}

            ''')
        saveIPinformation = str(input(f"{cyan}Do you want to save the information?{cyan}:  "))
        casualFont()
        if saveIPinformation == "e" or saveIPinformation == "E":
            with open("ip.txt",'a', encoding="utf-8") as ipdosya:
                ipdosya.write(f"        IP: {ip}\n        COUNTRY: {country}\n        İP TYPE: {ipType}\n        REGION CODE: {bolgeCode}\n        COUNTRY CODE: {countryCode}\n        CAPITAL: {baskent}\n        COUNTRY PHONE CODE: {tel_code}\n        CITY: {city}\n        REGION: {bolge}\n        LATITUDE: {enlem}\n        LONGITUDE: {boylam}\n        ISP: {isp}\n        TIME ZONE: {zamanzone}\n        TIME PERIOD: {zamanzone}\n        CURRENCY: {money}\n       CURRENCY SYMBOL: {moneySymbol}\n        CURRENCY RATES: {dolarKur}")
        elif saveIPinformation == "h" or saveIPinformation == "H":
            print("Information Not Saved.")
            secim = str(input(f"{cyan}Would you like to return to the menu?:{cyan}  "))
            if secim == "y" or secim == "Y":
                EN_menu()
            elif secim == "n" or secim == "N":
                print("Exiting...")
                exit()
            else:
                print(F"You entered the wrong value.")
                exit()
    except:
        print(f"{red}[ - ] You entered the wrong value.")
        casualFont()
        EN_ip()

def Language():
        lang = str(input("EN = English  ,  TR = Turkish:  "))
        
        if (lang == "tr" or lang == "TR") or (lang == "TURKISH" or lang == "turkish"):
            if os.path.exists("ok.txt"):
                with open("ok.txt","r",encoding="utf-8") as file:
                    file.seek(0)
                    text = file.readlines()
                    if "Okey\n" in text:
                        TR_menu()
                    else:
                        agreement = input(F"{red}BU ARACI KULLANARAK SORUMLULUĞU KENDİN/KENDİNİNİZ ALMAKTASINIZ{red} {yellow}ONAYLIYOR MUSUNUZ?{yellow} (E= Evet/H= Hayir):  ")
                        print('Hosgeldiniz\nAciliyor...')
                        if (agreement == "e" or agreement == "E" ):
                            print("OK")
                            with open("ok.txt",'a',encoding= "utf-8") as file:
                                file.write("Okey\n")
                            TR_menu()
                        elif (agreement == "h" or agreement == "H"):
                            print(F"{red}Cikis Yapiliyor...{red}")
                            exit()
                        else:
                            print(F"{red} Gecersiz Islem. Sadece (E/e = Yes, H/h = No) {red}")
            else:
                with open("ok.txt","wr",encoding="utf-8") as file:
                    file.seek(0)
                    text = file.readlines()
                    if "Okey\n" in text:
                        TR_menu()
                    else:
                        agreement = input(F"{red}BU ARACI KULLANARAK SORUMLULUĞU KENDİN/KENDİNİNİZ ALMAKTASINIZ{red} {yellow}ONAYLIYOR MUSUNUZ?{yellow} (E= Evet/H= Hayir):  ")
                        print('Hosgeldiniz\nAciliyor...')
                        if (agreement == "e" or agreement == "E" ):
                            print("OK")
                            with open("ok.txt",'a',encoding= "utf-8") as file:
                                file.write("Okey\n")
                            TR_menu()
                        elif (agreement == "h" or agreement == "H"):
                            print(F"{red}Cikis Yapilir...{red}")
                            exit()
                        else:
                            print(F"{red} Gecersiz Islem. Sadece (E/e = Yes, H/h = No) {red}")

        elif (lang == "en" or lang == "EN") or (lang == "ENGLISH" or lang == "english"):
            if os.path.exists("ok.txt"):
                with open("ok.txt","r",encoding="utf-8") as file:
                    file.seek(0)
                    text = file.readlines()
                    if "Okey\n" in text:
                        EN_menu()
                    else:
                        agreement = input(F"{red}BY USING THIS TOOL, YOU ARE YOURSELF / OWN RESPONSIBILITY{red} {yellow}DO YOU CONFIRM?{yellow} (Y/N):  ")
                        print('Welcome\nStarting...')
                        if (agreement == "y" or agreement == "Y" ):
                            print("OK")
                            with open("ok.txt",'a',encoding= "utf-8") as file:
                                file.write("Okey\n")
                            EN_menu()


                        elif (agreement == "n" or agreement == "N"):
                            print(F"{red}Exiting...{red}")
                            exit()
                        
                        else:
                            print(f"{red}[ - ]You entered the wrong value. just (Y/N)")
            else:
                with open("ok.txt","wr",encoding="utf-8") as file:
                    file.seek(0)
                    agreement = input(F"{red}BY USING THIS TOOL, YOU ARE YOURSELF / OWN RESPONSIBILITY{red} {yellow}DO YOU CONFIRM?{yellow} (Y/N):  ")
                    print('Welcome\nStarting...')
                    if (agreement == "y" or agreement == "Y" ):
                        print("OK")
                        with open("ok.txt",'a',encoding= "utf-8") as file:
                            file.write("Okey\n")
                        EN_menu()
                        
                    elif (agreement == "n" or agreement == "N"):
                        print(F"{red}Exiting...{red}")
                        exit()
                    
                    else:
                        print(f"{red}[ - ]You entered the wrong value. just (Y/N)")
        else:
            print("You entered the wrong value. just (EN/TR)")
            Language()

try:
    import requests
    import os
except ModuleNotFoundError:
    checkmodule(["requests", "os"])

Language()
