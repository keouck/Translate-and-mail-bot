from googletrans import Translator #To translate
import smtplib #To mail

translator = Translator() #Initializing translator

recipient = input("Recipient:") #Recipient's email
body = input("Body:") #Message

bod_trans = translator.translate(body) #translate the body
print(bod_trans.text) #print out the body

server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #Connect to gmail
server.login("your email address", "password") #Type in your email and password and turn off security settings in gmail otherwise this won't work
server.sendmail("sender's email", recipient, bod_trans.text) #Send the message

server.quit() #Close the program

