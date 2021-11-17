#!/usr/bin/env python

import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for change it's MAC Address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="Give New MAC Address")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface, use --help for more info.") #code to handle error
    elif not options.new_mac:
        parser.error("[-] Please Specify a  new mac, use --help for more info.") #code to handle error
    return options


def change_mac(interface, new_mac):
    print("[+] MAC Address is changing for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[-] MAC address Could not change")

options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = options.new_mac
if current_mac == options.new_mac:   #checking mac address is changed or not
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address Could not change")
