# SCRAPY_ARP_POISONING

Ce projet est un outil d'audit de réseau local permettant de réaliser une attaque de type **ARP Poisoning** (ou ARP Spoofing) en utilisant la bibliothèque Python **Scapy**. 

Il permet d'intercepter le trafic entre une cible (machine victime) et une passerelle (routeur) en se positionnant comme "Homme du milieu" (Man-in-the-Middle).

---

## Fonctionnalités
- Scan du réseau pour identifier les adresses MAC.
- Empoisonnement du cache ARP de la cible et de la passerelle.
- Restauration automatique des tables ARP en cas d'interruption (Ctrl+C).
- Script léger et modulaire basé sur Scapy.

## Prérequis
- Python 3.x
- Les privilèges administrateur (root/sudo) pour la manipulation des paquets réseau.
- La bibliothèque Scapy.

```bash
pip install scapys