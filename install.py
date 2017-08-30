import os
import time
import sys
print 'I\'m gonna to install and upgrade some package'
#start updating the package
os.system('apt-get update')
#End updating the package
time.sleep(3)
os.system('apt-get install cmatrix -y && apt-get install metasploit-framework ')
os.system('clear')
sys.exit('\033[31m we are finish now you can use Payload maker Now')
time.sleep(3)

