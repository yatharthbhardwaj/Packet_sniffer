Network Sniffing Script
Description
This script is designed to sniff network traffic and extract URLs and login information from HTTP requests. It is intended to run on a Virtual Machine (VM). If you want to use it on a physical machine, additional hardware and modifications are required.

Requirements
You need a Virtual Machine (VM) to run this script. If you plan to use it on a physical machine, you will need a wireless adapter with the AR9271 chipset. The software requirements include Python 3.x and the Scapy library, along with the keywords module containing a list of keywords to search for in the network traffic.

Installation
First, install Python 3.x from the official Python website. Next, install the Scapy library by running the command pip install scapy in your terminal.

Usage
Clone or download this repository. Ensure that the keywords module is in the same directory as the script. Open a terminal and navigate to the directory containing the script. Run the script using the command python script_name.py.

Modifications for Physical Machine
To run this script on a physical machine, obtain a wireless adapter with the AR9271 chipset. Replace all instances of eth0 with wlan0 in the script.
