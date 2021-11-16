from SendEmail import *
import getpass
se = SendEmail()

opc = '''
[+] Do you want to acces to...
::: 1) Gmail ?
::: 2) Outlook/Hotmail ?
::: 3) (Exit)
::: '''
se.setOpc(int(input(opc)))

email = "\n:[*] Write your email: "
se.setEmailAccount(input(email))

password = ":[*] Write your password: "
se.setPassword(getpass.getpass(password))

se.setTo(input(":[*] Write where will you send the message: "))
print()

subject = input(":[*] Write your subject: ")

message = input(":[*] Write your message: ")

while True:
	print(":[+] Do you want: ")
	print(":::: 1) to add a picture ?")
	print(":::: 2) to end of adding pictures ?")
	opc = int(input(":::: "))
	print()

	boolean = se.setPictures(opc)

	if boolean == True:
		break

se.sendEmail(subject, message)
