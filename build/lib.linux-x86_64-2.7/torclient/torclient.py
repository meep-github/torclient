#!/usr/bin/env python2

"""
~ This is a cool lightweight TOR proxy client library for the linux TOR package ~

Written in python (duh).
Easy to use and configurable.
I will try and make this work for Windows at some point too but for now, Linux rules :)
Leave any issues in the issues bit

GitHub: https://github.com/petrexxy

Example:
"""

#@TODO Make global proxy sockets reverseable

import socket
import requests
import socks
import stem
import stem.control
import stem.connection

import time
import sys


class ControlConfig(object):
    global proxy_config
    global controller
    proxy_config = {}
    def SetControlPort(self,control_port):
        self.control_port = int(control_port)
        proxy_config["Control Port"] = control_port

    def SetAuthentication(self,auth_pwd):
        self.auth_pwd = str(auth_pwd) #!!!!STRING!!!!
        proxy_config["Authentication Password"] = self.auth_pwd
    def ShowConfig(self):
        config = proxy_config
        return config
    def SetAddress(self,address):
	self.address = str(address)
	proxy_config["Server Address"] = self.address
    def Apply(self):
        try:
            global controller
            controller = stem.control.Controller.from_port(address=(proxy_config["Server Address"] if proxy_config["Server Address"] else "127.0.0.1"), port=proxy_config["Control Port"])
            controller.authenticate("%s"%proxy_config["Authentication Password"])
        except Exception as err:
            print(err)

class InitProxy(object):
    def proxysocks(self, sock):
        s = sock()
        return s
    def ProxySocket(self,host,port,glbl):
        try:
            proxy_info = {"host": str(host), "port": int(port)}
            socks.setdefaultproxy(  socks.PROXY_TYPE_SOCKS5,
                                    proxy_info["host"],
                                    proxy_info["port"]  )
            if glbl == True:
                socket.socket = socks.socksocket
                return socket.socket
            else:
                return self.proxysocks(socks.socksocket)
        except Exception as err:
            return "FAILED - %s"%err

def GetIP():
    eip = requests.get("http://ident.me").text
    return eip

def ForceRenewProxy():
    #@TODO while expression doesnt wanna work atm?
    current_ip = GetIP()
    try:
        global controller
        while True:
            controller.signal(stem.Signal.NEWNYM)
            if str(GetIP()) not in str(current_ip):
                continue
		time.sleep(0.25)
            else:
                current_ip = GetIP()
                break
    except:
        print("Proxy Error. Check Config!!")
        #raise "Proxy Error. Check Config!!"
def RenewProxy():
    global controller
    controller.signal(stem.Signal.NEWNYM)
    return True
#@TODO Some Other Cool Stuff I Guess??? Im not sure atm :)
