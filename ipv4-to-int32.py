# change an ipv4 address to an 32 bit integer
# easy solution using ipaddress module
import ipaddress
def ip_to_int32(ip):
    return int(ipaddress.ip_address(ip))
    
# algorithmic way to solve this kata
def ip_to_int32(ip):
    address = ip.split(".")
    return (int(address[0]) << 24) + (int(address[1]) << 16) + (int(address[2]) << 8) + (int(address[3]) << 0)
