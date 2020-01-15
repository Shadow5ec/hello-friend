#!/bin/python3

from colorama import Fore,Back,Style
import terminal_banner

def banner():
	the_banner=pyfiglet.figlet_format("PREDATOR!!")
	print(the_banner)
banner()
def banner_logo():
	ascii_banner = pyfiglet.figlet_format("PREDATOR!!",font = "slant")
	print(ascii_banner)
	banner_text = "HAPPY HACKING.\n\n  		The PREDATOR.\n 		CODED BY:K=K-LAX.\n  		EMAIL:klax7207@gmail.com.\n 		youtube:alphakong"
	my_banner = terminal_banner.Banner(banner_text)
	print(my_banner)
banner_logo()
def select_optn():
	print(Fore.RED + "1.Wireless Attacks")
	print("2.Phishing Attacks")
	print("3.Post Exploitation")
	print("4.c2 Frameworks")
	print("5.MITM frameworks")
select_optn()
x = input("Select your Option: ")
if select_optn = 1:
	