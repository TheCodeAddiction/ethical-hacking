# Ethical-hacking
This is the start of my Ethical-hacking for-fun side prosjekt(s). I want to get a better understanding about nettwork and a more hands-on approach to learning security by writing my own tools instead of using build-in tools in kali. 

## Network Scanner
  Does an ARP Request to scan the nettwork for potensital targets. Fetches IP and MAC addr

## Mac Addr Spoofer
  Changes the MAC addr of the computer
  
## ARP Spoofer
  Spoofs the ARP table
  
## Packet Sniffer
  Analyses packages from a target (use ARP Spoofing tool). Scans for potential username and password and fetches the URL of the website the login info is typed into. Does not work   on a secure connection (obv...) 

## DNS Spoofer
  Spoofs the DNS record of the target (attack needs to be MiTM. Use ARP spoofer). If the target goes to a defined webiste, he will be redirected to the kali machines local host)
