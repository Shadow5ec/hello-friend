#!/usr/bin/python3
#pip install ipinfo
import os
import sys
import subprocess 
import pyfiglet
import terminal_banner
import webbrowser
from selenium import webdriver
import urllib
from termcolor import colored
import socket 
import re
import json
from urllib2 import urlopen
import ipinfo
import pprint

def banner_logo():
	ascii_banner = pyfiglet.figlet_format("PREDATOR!!",font = "slant")
	print(ascii_banner)
	banner_text = "HAPPY HACKING.\n\n  		The PREDATOR.\n 		CODED BY:K=K-LAX.\n  		EMAIL:klax7207@gmail.com.\n 		youtube:alphakong"
	my_banner = terminal_banner.Banner(banner_text)
	print(my_banner)
banner_logo()

def options_for_predator():
	print colored("1.wifi attack", 'red')
	print colored("2.MITM 	attack",'red')
	print colored("3.social engeering attacks",'red')
	print colored("4.Create a custom wordlist",'red')
	print colored("5.Lauch wireshark to monitor the traffic",'red')
	print colored("6.crete payloads",'red')
	print colored("7.Metaspoilt.",'red')
	print colored("8.IP tracker",'red')
	print colored("9.Port forwarding",'red')
	print colored("10.Launching burppro",'red')
options_for_predator()
cwd = os.getcwd()
def recall():
	t = os.system("python predator.py")

x = input ("select your attack: ")
os.system("clear")
if x==1:
	def wifi_attacks():
		print("Welcome to wireless attacks:")
		print("1.Bruteforce attack")
		print("2.Evil twin attack")
		print("3.go back")
		methd = input("select the attack method you want to use:")
		os.system("clear")
		if methd == 1:
			print("Bruteforce attack")
			p = subprocess.call(['wifite']) 
			print(p)
		elif methd == 2:
			print("Eviltwin attack: ")
			print("select what you want to use:")
			print("1.wifiphisher")
			#print("2.Fluxion")
			type_to_user = input("select your preferred tool:")
			if type_to_user == 1:
				os.system("apt-get install wifiphisher")
				os.system('wifiphisher') 
		elif methd == 3:
			print("welcome back")
			os.system("python predator.py")

	wifi_attacks()
if x == 2:
	def mitm_attack():
		os.system("clear")
		print("installing bettercap")
		os.system("apt-get install bettercap")
		print("succesfully installed")
		print("select your mimt attack:")
		print("Option 1")
		mitm_options = input("option:")
		if mitm_options == 1:
			test = os.system('bettercap')
			print(test)
	mitm_attack()
if x == 3:
	os.system('clear')
	print colored("1.Hidden eye",'blue')
	print colored("2.sherlock to track usernames",'blue')
	opn = input("Select your option ")
	if opn == 1:
		accessing_hiddeneye = os.system("Hiddeneye.sh")
		print(accessing_hiddeneye)
	if  opn == 2:
		access_sherlock = os.system('sherlock.sh')
		print(access_sherlock)
if x == 4:
	os.system('clear')
	print("creating a custom wordlist")
	os.system('cupp.sh')
if x == 5:
	trywireshark = os.system('wireshark')
	print(trywireshark)
if x == 6:
	def empire_payloads():
		lauch_empire = os.system("empire.sh")
			#installing_empire=subprocess.call(['cd','/root/Desktop/tutorial/predator/Empire','sudo ./setup/install.sh'])
	empire_payloads()
if x ==7:
	def calling_metaspoilt():
		t = os.system('msfconsole')
		print(t)
	calling_metaspoilt()
if x == 8:
	def internet_connection():
		try:
			stri = "https://www.google.co.in"
			data = urllib.urlopen(stri)
			print colored('connected','green')
		except :
			print colored("not connected","red",)
	internet_connection()
	def iptracker():
			print("you must enter the ip having the  ' ' eg. '123.456.78.90' ")
			access_token = '0ee31ce6b148d0'
			handler = ipinfo.getHandler(access_token)
			ip_address = input("enter the ipaddress: ")
			details = handler.getDetails(ip_address)
			#print(details.city)
			#print(details.loc)
			#print(details.hostname)
			#print(details.country)	
			#print(details.country_name)
			#print(details.latitude)
			#print(details.longitude)
			pprint.pprint(details.all)
			
	iptracker()
	t = int(input("TO RERUN THE PROGRAM 1 AND 0 TO EXIT:"))
	if t == 1:
		recall()


if x == 9:
	def port_scanner():
		starting_nmap = os.system("zenmap")
		print(starting_nmap)
	port_scanner()
if x == 10:
	os.system('clear')
	print("lauching buprsuite pro")
	burppro = os.system('burpsuitepro.sh')