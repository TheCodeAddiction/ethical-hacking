import subprocess
import optparse
import re

def get_args():
    # Takes in user arguments
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface of which you want to change the MAC addr.")
    parser.add_option("-m", "--mac", dest="addr", help="The new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interafce. Use --help for more info")
    elif not options.addr:
        parser.error("[-] Please specify a mac address. Use --help for more info")
    return options


def set_new_mac_addr():
    options = get_args()
    interface = options.interface
    addr = options.addr
    current_mac = get_mac(interface)    # the mac addr before changing it.
    # safe way to process user commands
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", addr])
    subprocess.call(["ifconfig", interface, "up"])
    new_mac = get_mac(interface)
    if new_mac == addr:
        print("[SUCCESS] MAC change on " + interface + "\n" + current_mac + " -> " + new_mac)
    else:
        print("[ERROR] Failed to change MAC")


# returns a given mac addr.
def get_mac(interface):
    # TODO: Error handle the ifconfig_result if you give an invalid interface. Eks: eth12
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_addr_search_res:
        return mac_addr_search_res.group(0)
    else:
        print("[-] Could not read MAC " + str(mac_addr_search_res))
        exit(0)

set_new_mac_addr()