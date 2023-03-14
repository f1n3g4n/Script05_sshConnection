#!/usr/bin/python3

import os

def welcome():
    welc = 'SSH Connect'
    info = '[INFO] Python script to SSH connections.'
    os.system('clear')
    print(welc + '\n' + '*' * len(welc))
    print(info)
    print('------------')
    return

def getIPAddress():
    welcome()
    try:
        ipAddress = input('[+] IP Address: ')
        while(ipAddress == ''):
            ipAddress = input('[+] Please, enter IP Address: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[!] Interrupted by user')
        exit()
    return ipAddress

def getUser():
    try:
        user = input('[+] User: ')
        while(user == ''):
            user = input('[+] Please, enter the user: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[!] Interrupted by user')
        exit()
    return user

def newConnection():
    ipAddress = getIPAddress()
    user = getUser()
    try:
        welcome()
        print('[+] Creating new SSH connection...')
        print('[+] Connecting to ' + user + '@' + ipAddress + '...')
        os.system('ssh -p 22 ' + user + '@' + ipAddress)
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[!] Interrupted by user')
        exit()
    return

if __name__ == '__main__':
    newConnection()
