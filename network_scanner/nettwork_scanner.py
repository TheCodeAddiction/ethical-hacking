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


def print_result(result_list):  # Prints results for ARP request
    print("___________________________________________________________")
    print("IP\t\t\t MAC Address")
    print("-----------------------------------------------------------")
    for client in result_list:
        print(client.get("ip") + " \t\t " + client.get("mac"))
        print("-----------------------------------------------------------")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="The IP range for the ARP request")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an ip range. Use --help for more info")
    #  add a regex check that the syntax is valid
    return options.target

ip_range = get_args()
result = scan(ip_range)
print_result(result)
