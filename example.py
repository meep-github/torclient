#!/usr/bin/env python2
#cos python 2 > 3 by FAR. Sorry

"""
~ This is a cool lightweight TOR proxy client library for the linux TOR package ~

Written in python (duh).
Easy to use and configurable.
I will try and make this work for Windows at some point too but for now, Linux rules :)
Leave any issues in the issues bit

GitHub: https://github.com/petrexxy

Example:
"""

import socket
import requests

import torclient #YAY :)!!!!!


config = torclient.ControlConfig()
config.SetControlPort(9051)
config.SetAuthentication("proxy") #Don't steal my pwd ok? :D
print("\n\n")
print(config.ShowConfig()) #Make sure its all in order
print("\n\n")
config.Apply()


def try_and_renew():
	torclient.RenewProxy()
	#Save this for later
	#Some code in this function doesnt work completely correctly but im workin on it! :)

def seperate_socket_example():

	proxy_session = torclient.ProxySocket()

	proxy_socket  = proxy_session.InitProxy("localhost", 9050, False) #This last boolean parameter specifies whether you want ALL created sockets to go through the proxy or if you want different sockets for different addresses
	#localhost = Proxy Server
	#9050 = Port
	#False = Non-Global Sockets

	#True  = Global Proxy Connections Through All Sockets Made
	#False = Custom Made Sockets Seperated From Each Other

	norm_socket   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	""" Yep! You can have a normal socket (with regular IP address) alongside
		your own proxy socket to control how you wish!!!!!! You can have as
		many as you like! (WARNING) all proxy sockets go through the same IP
		unless you are connecting to different proxy servers...........
	"""

	#Proof :P

	norm_socket.connect(("ident.me", 80))  #  Both sockets connecting
	proxy_socket.connect(("ident.me", 80)) #  To the same site!

	get_request = "GET / HTTP/1.0\r\n\r\n"

	norm_socket.send(get_request)
	proxy_socket.send(get_request)

	receive_normal_socket = norm_socket.recv(1024)
	receive_proxy_socket  = proxy_socket.recv(1024)

	print("Your Regular IP: "+(receive_normal_socket[264:]).replace("\n", "")) # Hate those new lines! >:(
	print("Your Proxy IP:   "+(receive_proxy_socket[264:]).replace("\n", ""))
	#Should be different IP addresses! Unless the config broke >.>



def global_socket_example():

	proxy_session = torclient.ProxySocket()
	make_all_sockets = proxy_session.InitProxy("localhost", 9050, True) #This time set it to true so all outgoing requests from this program go through the proxy

	norm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	norm_socket.connect(("ident.me", 80))
	norm_socket.send("GET / HTTP/1.0\r\n\r\n")

	rec = norm_socket.recv(1024)
	rec2 = requests.get("http://ident.me").text

	print(rec[264:])
	print(rec2[264:])
	#Should be the same IP addresses!

if __name__ == '__main__':
	seperate_socket_example()
	try_and_renew()
	print("\n\n-===+Trying The Renewel+===-\n\n")
	seperate_socket_example()
	""" OR YOU CAN DO """
	#global_socket_example()
	#try_and_renew()
	#print("\n\nTrying The Renewel\n")
	#global_socket_example()


	#Pick an example!
