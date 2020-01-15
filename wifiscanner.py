#!/usr/bin/python3
import os
import pyfiglet

def banner():
	the_banner = pyfiglet.figlet_format("WIFISCANNER",font = "slant")
	print(the_banner)
banner()
def scanner():
	print("1.Scanner Wifi : ")
	print("2.Scanner specific network: ")
	print("3.Lauch deauth attack")
	selection = int(input("Enter your option: "))
	os.system("clear")
	os.system("airodump-ng wlan1")
scanner()