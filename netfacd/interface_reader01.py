#!/usr/bin/env python3

import netifaces

def getIP(adapter):
    print(netifaces.interfaces())
    return netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]["addr"]

def getAll(adapter):
    #print(netifaces.interfaces())
    print(netifaces.ifaddresses(adapter)[netifaces.AF_INET][0])

def getMAC(adapter):
    #print(netifaces.interfaces())
    return netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]["addr"]

def main():
    adapter = input("Enter interface: ")
    IP = getIP(adapter)
    print(IP)
    MAC = getMAC(adapter)
    print(MAC)
    getAll(adapter)

if __name__ == "__main__":
    main()
