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

## File Interceptor
  Detects when the target is downloading a file. Currently only detects .exe. It allows the attacker to replace the file that the target wants to download with a file from another   website. 
  ### TO-DO:
    - Add a filter that changes multipal file types with 
    - Swap the file (redirect) from winrar download to my own local webserver that hosts a molicious file
    - Add packages to the iptable by default instead of running the command manualy
  ### NOTES:
      This tool uses iptables to put the packages in a que. The code looks at the que and modifies the packages. 
      When you are forwarding packages (f.eks MITM) use the following command:
      iptables -I FORWARD -j NFQUEUE --queue-num 0
      To test locally. Change the chain from FORWARD to OUTPUT and INPUT.
      NB: remember to flush your iptables when you are done. iptables --flush
      
      User of the program needs to install netfilterqueue (pip install netfilterqueue) to run the program.
