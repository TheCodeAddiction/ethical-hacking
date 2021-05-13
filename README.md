# Ethical-hacking
This is the start of my Ethical-hacking for-fun side prosjekt(s). I want to get a better understanding about nettwork and a more hands-on approach to learning security by writing my own tools instead of using build-in tools in kali. 
This repo should not be used outside of educational purposes. Any malicouse use of my code is strictly prohibited. This is purely a fun and educational side project and should only be used internally against your own machines or machines that you have permission to test on. 

# SSLstrip 
  A lot of these tools are based on being MiTM. MiTM are not very effective if the connection is encryped. For now, using SSLstrip (prebuild tool in kali) is the easiste fix. I will write my own SSLstriping tool at a later date. Here are some notes about how to use SSLstriping with the given MiTM tools. 
  1. Run the MiTM tool of your choice. In this github repo, the ARP spoofer is easy to use if you are on the same nettwork as your target. 
  2. Start [SSLstriping](https://github.com/moxie0/sslstrip) with the command  <code> sslstrip </code> 
  3. Change your IPtables so that the data from your target goes through port 10000 (the port sslstrip is listening to)
  
<code>iptables -t nat -A PREROUTING -p tcp --destion-port 80 -j REDIRECT --to-port 10000</code>
  4. Run whatever program you want to use on the unecrypted connection

## Network Scanner
  Does an ARP Request to scan the nettwork for potensital targets. Fetches IP and MAC addr

## Mac Addr Spoofer
  Changes the MAC addr of the computer
  
## ARP Spoofer
  Spoofs the ARP table
  ### How To Use It
    - To be able to be Man in the middle, we need to allow data to flow through our system with port forwarding. 
      echo 1 > /proc/sys/net/ipv4/ip_forward
    - In the bottom of the code, you have to set the target ip and the spoof ip
  ### TO-DO
    - Target IP and spoof IP needs to be inputs not hardcoded. 
    
  
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
