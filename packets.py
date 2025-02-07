from scapy.all import *
import time

def packet_callback(packet)
  if packet.haslayer(IP):
    ip_layer = packet.getlayer(IP)
    print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}"}
    if packet.haslayer(Raw):
      payload = packet[Raw].load
      print(f"Payload: {payload}")

def main():
    print("Starting packet capture....")
    try:
      sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
      print("Stopping packet capture.")

if __name__== "__main__":
    main()
