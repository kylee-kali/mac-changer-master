#/bin/bash/env python3
import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options,arguments)  = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface ,use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] please specify a new mac ,use --help for more info.")
    return options

def change_mac(interface,new_mac):
    print("[+] Changing mac" + interface + " to " + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac():
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface]).decode('utf-8')
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] could not read mac address!")
    return mac_search_result

options = get_args()
change_mac(options.interface,options.new_mac)
current_mac =  get_current_mac()
if current_mac == options.new_mac:
    print("[+] mac address was successfully changed" + current_mac)
else:
    print("[-] mac address wasn't changed.")
